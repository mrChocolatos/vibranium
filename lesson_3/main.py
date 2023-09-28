import csv
import json


def main():

    data, __ = read_csv("books.csv")
    count_books = len(data)
    users = read_json_file("users.json")
    row = iter_books(data)
    while count_books != 0:
        for user in users:
            if count_books == 0:
                break
            user["books"].append(next(row))
            count_books -= 1
    write_json_file(users)


def iter_books(file):
    for item in file:
        yield item


def read_json_file(path: str):
    with open(path, 'r') as file:
        users = json.load(file)
        groom_users_json_file(users)
    return users


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
    return users_file


def write_json_file(users_with_books):
    with open("result.json", "w") as file:
        groom_books_list(users_with_books)
        file.write(json.dumps(users_with_books, indent=4))


def groom_books_list(users_file):
    for item in users_file:
        for book in item["books"]:
            for key in list(book.keys()):
                if key not in ["title", "author", "pages", "genre"]:
                    del book[key]
    return users_file


if __name__ == '__main__':
    main()
