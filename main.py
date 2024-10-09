import time
from tasks import add

result = add.delay(4, 4)

while not result.ready():
    time.sleep(1)

print(result.get())
