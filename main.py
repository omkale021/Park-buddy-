def main():
    # Step 1: Capture license plate
    license_plate_image = capture_license_plate()
    cv2.imwrite('license_plate.jpg', license_plate_image)

    # Step 2: Predict license plate (assuming model is already trained)
    predicted_license_plate = predict_license_plate(model, 'license_plate.jpg')
    print(f"Predicted License Plate: {predicted_license_plate}")

    # Step 3: Send payment request
    payment_response = send_payment_request('user_123', 50)
    print(payment_response)

    # Step 4: Confirm payment and allocate slot
    payment_confirmation = confirm_payment(payment_response['transaction_id'])
    if payment_confirmation['status'] == 'success':
        allocated_slot = allocate_parking_slot()
        if allocated_slot:
            print(f"Parking slot allocated: {allocated_slot}")
        else:
            print("No parking slots available")
    else:
        print("Payment failed")

if __name__ == "__main__":
    main()
