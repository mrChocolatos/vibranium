import csv
import json


def main():

    data, __ = read_csv("books.csv")
    count_books = len(data)
    users, user_count = read_json_file("users.json")
    row = iter_books(data)
    while count_books != 0:
        for user in users:
            if count_books == 0:
                break
            user["books"].append(next(row))
            count_books -= 1
    groom_users_json_file(users)
    with open("result.json", "w") as file:
        file.write(json.dumps(users, indent=4))


def iter_books(file):
    for item in file:
        yield item


def read_json_file(path: str):
    with open(path, 'r') as file:
        users_file = json.load(file)
        groom_users_json_file(users_file)
        count = len(users_file)
    return users_file, count


def read_csv(file_path):
    with open(file_path, "r", encoding="utf-8-sig") as file:
        csv_file = csv.DictReader(file, fieldnames=["title", "author", "genre", "pages"])
        headers = next(csv_file)
        return list(csv_file), headers


def groom_users_json_file(users_file):
    for item in users_file:
        for key in list(item.keys()):
            if key not in ["name", "gender", "address", "age", "books"]:
                del item[key]
                item["books"] = []
        for book in item["books"]:
            for key in list(book.keys()):
                if key not in ["title", "author", "pages", "genre"]:
                    del book[key]
    return users_file


if __name__ == '__main__':
    main()
