# fake_data_generator.py

from faker import Faker

# Create a dictionary of Faker locales for different countries
locales = {
    "India": "en_IN",   # English (India)
    "UAE": "en_US",     # No dedicated UAE locale, so we'll use en_US (can add Arabic support)
    "USA": "en_US",     # English (USA)
    "UK": "en_GB"       # English (Great Britain)
}

def generate_fake_data(country="India", count=5):
    """Generate fake names, emails, and addresses for a given country"""
    if country not in locales:
        print(f"❌ Country '{country}' not supported! Choose from: {list(locales.keys())}")
        return
    
    fake = Faker(locales[country])
    
    print(f"\n📍 Generating {count} fake profiles for {country}:\n")
    
    for i in range(count):
        name = fake.name()
        email = fake.email()
        address = fake.address().replace("\n", ", ")
        print(f"{i+1}. Name: {name}\n   Email: {email}\n   Address: {address}\n")


# Example usage
if __name__ == "__main__":
    generate_fake_data("India", 3)
    generate_fake_data("USA", 3)
    generate_fake_data("UK", 3)
    generate_fake_data("UAE", 3)
