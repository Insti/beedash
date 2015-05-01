# Your auth token from https://www.beeminder.com/settings/advanced_settings
# Don't share this with people unless you want them to be able to control
# your account!

BEEMINDER_AUTH_TOKEN = ''

# If you didn't set it above, load it from an environment variable.
if BEEMINDER_AUTH_TOKEN == '':
    import os
    BEEMINDER_AUTH_TOKEN = os.environ['BEEMINDER_AUTH_TOKEN']


