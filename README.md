# Dynaconf and Local Secrets

This application exists so I can try out [Dynaconf](https://www.dynaconf.com). Of possible interest to others is the 
code to load encrypted properties. The general use case is for a team that needs to share secrets for a local 
development environment. This allows the team to share only a single key where the remaining properties can be 
encrypted and stored in a file added to a repository. While it is not suitable for production secrets, it's good enough 
for handling secrets when running on a developer's machine.

## Running

The application requires a few environment variables:

- ENV_FOR_DYNACONF tells the application what environment you're running in. This should be `development` or `production` for this sample.
- DYNACONF_DECRYPT_KEY is the encryption and decryption key. See below on how to generate this for your application.
- LOADERS_FOR_DYNACONF should have the value `['dcws.secrets_loader', 'dynaconf.loaders.env_loader']`

`ENV_FOR_DYNACONF` and `LOADERS_FOR_DYNACONF` are defined in the [.env](.env) file. The application loads this file
automatically as the `load_dotenv` parameter is set to `True` in [config.py](dcws/config.py).

`DYNACONF_DECRYPT_KEY` is set by reading the value from standard input. The section below describes how to generate
this value.

## Bootstrapping

Because you do not have my encryption/decryption key, running the application out of the box will not allow
you to decrypt the encrypted properties.

Run the application with the command `./dcws.py -b`. This will spit out a new key and an encrypted value. Remove the "b"
and the single quotes surrounding the key and place that value in a file called [.secret](.secret). This file will be
ignored by Git. Replace the encrypted properties in [settings.yaml](dcws/resources/settings.yaml) with the encrypted 
value. For these, include the surrounding "ENC" and parentheses.

Once you have bootstrapped the application, you can run it with `cat .secret | ./dcws.py`. The application will print out both
the plain text of the encrypted property and the non-encrypted property.

# Changing environments

In a running application, you would set the `ENV_FOR_DYNACONF` variable outside the application. For this sample, you
can update the value in the [.env](.env) file to use the other environment.