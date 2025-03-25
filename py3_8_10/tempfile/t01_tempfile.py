import tempfile

if __name__ == "__main__":
    with tempfile.TemporaryFile(mode='w+') as t:
        t.write('hello')
        t.seek(0)
        print(t.read())
