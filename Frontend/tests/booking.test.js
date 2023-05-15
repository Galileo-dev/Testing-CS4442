// import { fireEvent, render, screen } from '@testing-library/svelte';
// import Form from '../src/lib/Booking.svelte';
// import { axe, toHaveNoViolations } from 'jest-axe';

// describe('Form', () => {
//   test('submits the form when all fields are valid', async () => {
//     // Render the form component
//     const { component } = render(Form);

//     // Fill out the form fields
//     const nameInput = screen.getByLabelText('Name');
//     const emailInput = screen.getByLabelText('E-mail');
//     const phoneInput = screen.getByLabelText('Phone Number');
//     const checkinInput = screen.getByLabelText('Check-in Date');
//     const checkoutInput = screen.getByLabelText('Check-out Date');
//     const adultsInput = screen.getByLabelText('Number of People');
//     const roomSelection = screen.getByLabelText('Select Room Preference');
//     const messageInput = screen.getByLabelText('Specifications');

//     fireEvent.input(nameInput, { target: { value: 'John Doe' } });
//     fireEvent.input(emailInput, { target: { value: 'johndoe@example.com' } });
//     fireEvent.input(phoneInput, { target: { value: '555-555-5555' } });
//     fireEvent.input(checkinInput, { target: { value: '2023-06-01' } });
//     fireEvent.input(checkoutInput, { target: { value: '2023-06-03' } });
//     fireEvent.input(adultsInput, { target: { value: 2 } });
//     fireEvent.change(roomSelection, { target: { value: 'connecting' } });
//     fireEvent.input(messageInput, { target: { value: 'This is a test message.' } });

//     // Submit the form
//     const submitButton = screen.getByRole('button', { name: 'Book The Rooms' });
//     fireEvent.click(submitButton);

//     // Check that the form was submitted
//     await component.$component.submitForm();
//     expect(component.$component.submitted).toBe(true);
//   });
// });




// expect.extend(toHaveNoViolations);

// describe('Form accessibility', () => {
//   it('should have no accessibility violations', async () => {
//     const { container } = render(Form);

//     const results = await axe(container);

//     expect(results).toHaveNoViolations();
//   });
// });