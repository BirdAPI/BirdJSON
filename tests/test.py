from pprint import pprint

import birdjson


if __name__ == "__main__":
    js = birdjson.load_file("config.json")
    if js:
        print js.settings.mysql.config.test[0].hello.int
        print js.settings.mysql.config.test[1]._2.int
        pprint(vars(js))


