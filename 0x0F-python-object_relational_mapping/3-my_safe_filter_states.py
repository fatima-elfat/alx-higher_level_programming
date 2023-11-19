if __name__ == "__main__":
    q = "WHERE name LIKE BINARY {}".format("ff")
    print("SELECT * FROM states  {}".format(q))