# text-based-mini-games
Developed at HackTheMidlands 2019. Programmable SMS to create text based games with Twilio.

## How To Use:
1. Text ```/start``` to the Twilio phone number
2. Then reply to the text with ```/play [game]```. Replacing [game] with a game name
3. Play the game!
4. Use ```/reset``` to go back to the first menu. 

## How It Works
Using twilios programable text API to send webhooks to a heroku dyno web server. The dyno responds with a webhook with a reply which is sent to the user

## Future Plans
- [ ] Battleships
- [ ] Multi user functionality
- [ ] Better stability
- [ ] Better erroneous data handling
