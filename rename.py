import os

def main():
    folder = "894D7000"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"NYC {str(count)}.nef"
        src = f"{folder}/{filename}"
        dst = f"{folder}/{dst}"

        os.rename(src,dst)

if __name__ == '__main__':
    main()