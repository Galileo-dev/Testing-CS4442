export const addBooking = async (data: any, userToken: any) => {
	const res = await fetch('http://127.0.0.1:8000/add_booking/', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${userToken}`
		},
		body: JSON.stringify(data)
	});

	return res;
};
