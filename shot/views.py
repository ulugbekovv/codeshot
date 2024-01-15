import asyncio
from django.shortcuts import render
from carbon import Carbon

client = Carbon()


async def main(code):
    img = await client.create(code, language='auto', downloads_dir='media/')
    print(img)
    return img


async def home(request):
    image = None
    if request.method == 'POST':
        code = request.POST.get('code-text')
        image = await main(code)
    return render(request, 'insert.html', {'image': image})
