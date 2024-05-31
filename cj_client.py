import json


def dump_cookies_to_json(cookies):
    cookies_list = [cookie.get_cookie_dict() for cookie in cookies]
    with open("cookie_jar.json", 'w') as outfile:
        json.dump(cookies_list, outfile)


def send_request(option):
    with open("cj_service.txt", "w") as comm_file:
        comm_file.write(option)


def display_response():
    with open("cj_service.txt", "r") as output_file:
        output = output_file.readline()
        print(output)


def main():
    dump_cookies_to_json(cookies)
    while True:
        option = input("Enter 'id' if you'd like to see all cookies sorted by id.\n"
          "Enter 'type' if you'd like to review all cookies by type.\n"
                       "Enter 'done' to return to the main program.\n")
        request = option.lower()
        if request == "done":
            send_request(request)
            break
        if request not in ['id', 'type']:
            print("Opps, there is no such option. Please try again.")
        else:
            send_request(request)
            display_response()
