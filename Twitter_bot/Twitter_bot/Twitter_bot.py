
import tweepy


#Authenticate to Twitter
auth = tweepy.OAuthHandler("2Afu2b2nX2urF5bGkI9Llh6m3",
                           "CpjHP5dP84y7rNGEPuobA6RCzcCaFBFjBJZqhSGi5Jex51QBEV")
auth.set_access_token("501130053-tdxTbNAvGzw8thzLqOFzLzhdFAJXSTowmAlq7NeJ",
                      "ecogAWzWL2MYNwTqQlPgXG1axMxtiKgYMXrYpj3zWK82V")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
