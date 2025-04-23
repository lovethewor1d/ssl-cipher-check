import requests
import re

def normalize_cipher_name(cipher_name):
    """Normalize OpenSSL cipher name to IANA style."""
    # Replace '-' with '_' and prepend 'TLS_' if not present
    normalized = cipher_name.replace('-', '_')
    if not normalized.startswith('TLS_'):
        normalized = 'TLS_' + normalized
    return normalized

def get_cipher_info(cipher_name):
    """Get cipher strength info from ciphersuite.info."""
    # Normalize the cipher name to IANA format
    normalized_cipher = normalize_cipher_name(cipher_name)
    
    # Prepare the URL for the API query
    url = f"https://ciphersuite.info/api/cs/{normalized_cipher}/"
    
    try:
        # Send request to the ciphersuite.info API
        response = requests.get(url)
        
        if response.status_code == 200:
            # Parse the response
            data = response.json()
            
            # Retrieve the cipher security information
            strength = data.get(normalized_cipher, {}).get("security", "Cipher strength information not found.")
            return f"Cipher: {normalized_cipher} -> Strength: {strength}"
        else:
            return f"Error: Could not retrieve data for cipher {normalized_cipher}."
    
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to connect to ciphersuite.info. Details: {str(e)}"

def clean_cipher_name(cipher_name):
    """Remove unwanted characters and normalize the cipher name."""
    # Remove '|' and everything starting from '('
    cleaned_cipher = re.sub(r'\|', '', cipher_name)  # Remove '|'
    cleaned_cipher = re.sub(r'\s*\(.*$', '', cleaned_cipher)  # Remove text starting from '(' onwards
    cleaned_cipher = cleaned_cipher.strip()  # Remove any leading/trailing whitespace
    return cleaned_cipher

def main():
    # Get user input for cipher names, allowing for multiple ciphers separated by newlines
    print("Enter the OpenSSL cipher names (one per line). Press Ctrl+D (or Enter after empty line) when done:")
    
    # Read multiple lines of input (one cipher per line)
    ciphers = []
    while True:
        try:
            cipher_name = input()
            if cipher_name.strip() == "":
                break
            # Clean the cipher name before adding it to the list
            cleaned_cipher = clean_cipher_name(cipher_name)
            ciphers.append(cleaned_cipher)
        except EOFError:
            break
    
    if ciphers:
        # Process each cipher
        for cipher in ciphers:
            result = get_cipher_info(cipher)
            print(result)
    else:
        print("No ciphers entered. Exiting...")

if __name__ == "__main__":
    main()
