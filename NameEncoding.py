import time

class NameEncoding:
    def nameExtension(self, filePath):
        username = "jdvande"
        currentTime = time.strftime('%a%d%b%Y-%HH%MM%SS')
        extension = filePath + username + "-" + currentTime + ".png"

        return str(extension)