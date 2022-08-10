import datetime
import logging
import sys
from pathlib import Path

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    ElementNotVisibleException,
    NoSuchAttributeException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)

from modules.automate_whatsapp import WhatsAppSender
from modules.load_config import load_yaml_config
from modules.load_data import load_contacts, load_message
from modules.random_sleep import random_sleep
from modules.save_data import save_data
from modules.validate_input_data import (
    validate_contacts,
    validate_files,
    validate_message,
    validate_config,
)


def main() -> None:

    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Validate functions unsure that input data are in the right format
    # It will throw error if not.
    folder = validate_files(
        input("Veuillez entrer le dossier contenant les fichiers de configuration :")
    )

    config = validate_config(load_yaml_config(Path(folder).joinpath("config.yml")))

    contacts = validate_contacts(load_contacts(config["contacts_path"]))

    message = validate_message(load_message(config["message_path"]))

    logger.info(f"Message to be sent :\n{'-'*90}\n{message}\n{'-'*90}\n")
    # It seems that formating characters (e.g. *) are not
    # count in message character limit. The limit is only for
    # image caption.

    sender = WhatsAppSender(config["chrome_profile"])

    tracking_messages = []
    for contact in contacts:
        # If message already sent, just save the row
        tracking_data = contact.copy()
        if int(contact["Sent"]) == 0:
            tracking_data.update({"Sent": "False", "Time": datetime.datetime.today()})
            phone_number = contact["WhatsApp Number(with country code)"]
            name = contact["Saved Name"]

            logger.info(msg=f"Sending message to '{name}' at '{phone_number}'.")

            try:
                sender.send_message_whith_attachment(
                    name, phone_number, config["attachment_path"], message
                )

            except TimeoutException as e:
                logging.error(e)

            except NoSuchAttributeException as e:
                logging.error(e)

            except NoSuchElementException as e:
                logging.error(e)

            except ElementClickInterceptedException as e:
                logging.error(e)

            except ElementNotInteractableException as e:
                logging.error(e)

            except ElementNotVisibleException as e:
                logging.error(e)

            except StaleElementReferenceException as e:
                logger.error(e)

            except Exception as e:
                logger.exception(e)

            else:
                tracking_data.update(
                    {"Sent": "True", "Time": datetime.datetime.today()}
                )
                logger.info(
                    msg=f"Message sent successfully to '{name}' at {phone_number}."
                )

            finally:
                random_sleep()
                tracking_messages.append(tracking_data)

        else:
            tracking_messages.append(tracking_data)

    sender.chrome_driver.close()
    save_path = Path(folder).joinpath("tracking_messages.csv")
    save_data(tracking_messages, save_path)
    logger.info(f"Messages tracking data saved in {save_path}.")


if __name__ == "__main__":
    main()
