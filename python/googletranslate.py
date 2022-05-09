from googletrans import Translator

translator = Translator()

result = translator.translate("trình biên dịch")

print(result.src)
print(result.dest)
print(result.origin)
print(result.text)



