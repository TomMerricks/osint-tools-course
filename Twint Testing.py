import twint

# Configure Twint
twint_config = twint.Config()
twint_config.Username = "realDonaldTrump"
twint_config.Search = "great again"

# Run twint
twint.run.set_event_loop(twint_config)