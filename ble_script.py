from bluepy.btle import Scanner

# Scan for BLE devices
scanner = Scanner()
devices = scanner.scan(10.0)  # Scan for 10 seconds

# List all available devices with names (if available)
print("Found the following BLE devices:")
device_list = []
for device in devices:
    device_name = "Unnamed Device"
    for (adtype, desc, value) in device.getScanData():
        if desc == "Complete Local Name":
            device_name = value
    print(f"{device.addr} - {device_name}")
    device_list.append((device.addr, device_name))

# Now you can interactively choose a device by name
chosen_name = input("Enter the name of the device you want to connect to: ")

# Find the chosen device by name
chosen_device = None
for addr, name in device_list:
    if name == chosen_name:
        chosen_device = addr
        break

if chosen_device:
    print(f"Connecting to {chosen_name} ({chosen_device})...")
    # Now you can use the MAC address to connect
    from bluepy.btle import Peripheral

    # Connect to the device using the MAC address
    device = Peripheral(chosen_device)
    print(f"Connected to {chosen_name}.")

    # (Optionally) You can now proceed to interact with the device as needed
    # For example, subscribing to notifications or reading characteristics.
else:
    print("Device not found.")
