# Translating Whisp

We would love to make Whisp accessible to users all around the world! Whisp uses standard GNU `gettext` for its localization.

If you would like to translate Whisp into your native language, please follow the steps below.

## How to Contribute a Translation

Currently, we accept translations via Pull Requests on GitHub.

1. **Fork the Repository**: Start by forking the Whisp repository to your own GitHub account.
2. **Locate the Template**: In the `po/` directory, you will find a `whisp.pot` template file. This file contains all the original English strings used in the application.
3. **Create a Translation File**: 
   - If you are starting a brand new translation for a language, create a new `.po` file named after your language code (for example, `es.po` for Spanish or `fr.po` for French) based on the `whisp.pot` template. 
   - You can use tools like [Poedit](https://poedit.net/) or `msginit` from the command line to generate this file easily.
4. **Translate**: Open your `.po` file in Poedit or your preferred translation editor and translate the strings!
5. **Update Existing Translations**: If your language's `.po` file already exists, simply open it and fill in any missing or fuzzy strings.
6. **Submit a Pull Request**: Once you are happy with your translations, commit your `.po` file to your fork and open a Pull Request back to the main Whisp repository.

## Testing Your Translation

If you want to test your translation locally before submitting:
1. Ensure you have the `gettext` package installed on your system.
2. Run the build command (`flatpak-builder` or Meson). Meson will automatically compile your `.po` file into a `.mo` file.
3. Run the application to see your strings in action!

## Having Trouble?

If you want to translate but are unfamiliar with Git, `.po` files, or Pull Requests, please feel free to **open an Issue** on GitHub! We will be more than happy to help set up the files for you or manually merge your translated strings.

Thank you for helping bring Whisp to more people!
