from telethon import TelegramClient
import openai


openai.api_key = "YOUR_OPENAI_API_KEY"

client = TelegramClient('Session Name', "YOUR_API_ID", "YOUR_API_HASH")

prompt = ("""Generate a perfect message in order to get a reply from a human""")

def read_file(filename):
        with open(filename, 'r') as f:
            return f.read().splitlines()


async def main():
    # Connect to the Telegram server
    await client.start("YOUR_PHONE_NUMBER")

    list = ["user1", "user2", "user3", "user4", "user5", "user6"]
    # Or get the list of user from a file
    #list_file = read_file("users.txt")
    for i in list:
        try: 
            entity = await client.get_entity('@'+i)
            if entity:
                    response = openai.Completion.create(
                        engine="text-davinci-002",
                        prompt=prompt,
                        temperature=0.7,
                        max_tokens=60,
                        n=1,
                        stop=None,
                        frequency_penalty=0,
                        presence_penalty=0
                    )

                    message = response.choices[0].text.strip()

                    print(message)
                    await client.send_message(id, message)

            else:
                print(i + ':no')    
        except ValueError:
            print(i + ':no')
    
    # Disconnect the client
    await client.disconnect()

# Run the main function
with client:
    client.loop.run_until_complete(main())
