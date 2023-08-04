import openai

response = openai.Image.create_edit(
  image=open("myqr.png", "rb"),
  mask=open("myqr.png", "rb"),
  prompt="A sunlit indoor lounge area with a pool containing a flamingo",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']