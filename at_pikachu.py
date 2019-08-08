import os
import time
import re
from slack import RTMClient, WebClient


# instantiate Slack client
#slack_client = WebClient(token=slack_token)
# starterbot's user ID in Slack: value is assigned after the bot starts up
#pikachubot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "pika"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

def parse_bot_commands(slack_events):
    """
    Parses a list of events coming from the Slack RTM API to find bot commands.
    If a bot command is found, this function returns a tuple of commands and channel.
    If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == pikachubot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    """
    Finds a direct mention ( a mention that is at the beginning) in message text
    and returns the user ID which was mentioned. If there is no direct metnion, returns None, None.
    """
    matches = re.search(MENTION_REGEX, message_text)
    # first group contains the username, and the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel):
    """
    Executes bot command if the command is known
    """
    # default response is help text for the user
    default_response = "Pika? Pika pika pika (Try *{}*.".format(EXAMPLE_COMMAND)

    # finds and executes the given command, filling in response
    response = None

    # This is where you start to implement more commands
    if command.startswith(EXAMPLE_COMMAND):
        response = "Pikaaaa!"

    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )

@RTMClient.run_on(event='message')
def respond(**payload):
    print(payload)
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    
    if '<@ULU8GG2H3>' in data.get('text'):
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']

        web_client.chat_postMessage(
                channel=channel_id,
                text=f"Pika? ({data.get('text').lstrip('<@ULU8GG2H3> ')}?)"
        )
    if 'Mark' in data.get('text'):
        channel_id = data['channel']

        web_client.chat_postMessage(
                channel=channel_id,
                text="Pikaaapi"
        )
    if 'Rana' in data.get('text'):
        channel_id = data['channel']

        web_client.chat_postMessage(
                channel=channel_id,
                text="Pika pika!"
        )

if __name__ == "__main__":
    slack_token = os.environ["SLACK_BOT_TOKEN"]
    rtm_client = RTMClient(token=slack_token)
    rtm_client.start()
