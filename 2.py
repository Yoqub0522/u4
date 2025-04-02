import logging



class SafeLogFileManager:

    def __init__(self, filename):

        self.filename = filename

        self.file = None



    def __enter__(self):

        """ Faylni ochamiz va log yozish boshlanadi """

        self.file = open(self.filename, "w")

        self.file.write("📌 Log yozish boshlandi!\n")

        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

        return self.file



    def __exit__(self, exc_type, exc_value, traceback):

        """ Agar xato bo‘lsa, logga yozamiz """

        if exc_type:

            logging.error(f"❌ Xatolik: {exc_value}")

            self.file.write(f"❌ Xatolik yuz berdi: {exc_value}\n")



        """ Faylni yopamiz """

        self.file.write("✅ Log yozish tugadi!\n")

        self.file.close()

with SafeLogFileManager("loglar.txt") as logfile:

    logging.info("Bu INFO xabar")



    logging.warning("Bu WARNING xabar")