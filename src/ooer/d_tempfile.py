import tempfile

temp = tempfile.TemporaryDirectory()
print(temp)

print(tempfile.gettempdir())
