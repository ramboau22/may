import json
# import logging


# logging.basicConfig(level=logging.INFO, filename='%(asctime)s - %(levelname)s - %(message)s')
def save_data_to_json(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
    # logging.info("data is saved as json!!!")


def main():
    data = {}
    # logging.info("Data Inpur Applicaiton")
    while True:
        key = input("Enter a key (or 'q' to quite): ")
        if key == 'q':
            break

        value = input("Enter the value: ")
        data[key] = value
        # logging.info(f"Values entered for key '{key}': {value}")
    save_data_to_json(data)


if __name__ == '__main__':
    main()
