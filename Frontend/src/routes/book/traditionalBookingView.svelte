<script lang="ts">
	import { auth } from '$lib/firebase';
	import { userStore } from 'sveltefire';
	import { onMount } from 'svelte';
	import type { PageData } from './$types';
	import Modal from '$lib/Modal.svelte';
	import { addBooking } from '$lib/Booking';

	const user = userStore(auth);
	let userToken = '';
	user.subscribe((u) => {
		if (u) {
			u.getIdToken().then((t) => (userToken = t));
		}
	});

	let showModal = false;
	const handleToggleModal = () => {
		showModal = !showModal;
	};
	let modalContent = '';

	export let data: PageData;
	let rooms = data.rooms;

	const bookingHandler = async (e: Event) => {
		e.preventDefault();
		const form = e.target as HTMLFormElement;
		const formData = new FormData(form);
		const data = Object.fromEntries(formData.entries());

		// format datatime %d-%m %H:%M because server expects this format
		let checkin = new Date(data.checkin as string);
		data.checkin = `${checkin.getDate()}-${checkin.getMonth()} ${checkin.getHours()}:${checkin.getMinutes()}`;

		let body = {
			room_id: data.room_preference,
			date_time_str: data.checkin,
			length_in_mins: data.lengthofstay
		};

		let res = await addBooking(body, userToken);
		const json = await res.json();
		console.log(json);
		modalContent = json.message;
		showModal = true;
	};
</script>

<!-- make it 800px * 500px -->
<div class="flex items-center justify-center">
	<header>
		<h1>BookMe</h1>
		<nav>
			<a href="#">Something</a>
			<a href="#">Swag</a>
			<a href="#">Mike Tyson</a>
			<a href="#">Ghoul</a>
		</nav>
	</header>
</div>

<div class="divider" />
<div class="flex items-center justify-center">
	<form id="form" method="post" on:submit|preventDefault={bookingHandler}>
		<div class="elem-group">
			<label for="name">Name</label>
			<input
				type="text"
				id="name"
				name="visitor_name"
				placeholder="Name"
				pattern="[A-Z\sa-z]{(3, 20)}"
				value={$user?.displayName}
				disabled
				required
			/>
		</div>
		<div class="elem-group">
			<label for="email">E-mail</label>
			<input
				type="email"
				id="email"
				name="visitor_email"
				placeholder="example@gmail.com"
				value={$user?.email}
				disabled
				required
			/>
		</div>
		<div class="elem-group">
			<label for="phone">Phone Number</label>

			<input type="tel" id="phone" name="visitor_phone" placeholder="123-456-7890" required />
		</div>
		<hr />
		<div class="elem-group inlined">
			<label for="checkin-date">Check-in Date</label>
			<input type="datetime-local" id="checkin-date" name="checkin" required />
		</div>
		<div class="elem-group inlined">
			<label for="length-of-stay">Length of Stay (minutes)</label>
			<input
				type="number"
				id="length-of-stay"
				name="lengthofstay"
				placeholder="60"
				min="0"
				required
			/>
		</div>
		<div class="elem-group inlined">
			<label for="adult">Number of People</label>
			<input type="number" id="adult" name="total_adults" placeholder="2" min="1" required />
		</div>
		<div class="elem-group inlined">
			<label for="room-selection">Select Room to Book</label>
			<select id="room-selection" name="room_preference" required>
				{#each rooms as room}
					<option value={room.id}>{room.displayName}</option>
				{/each}
			</select>
		</div>
		<hr />
		<div class="elem-group">
			<label for="message">Specifications</label>
			<textarea
				id="message"
				name="visitor_message"
				placeholder="Tell us anything else that might be important."
				required
			/>
		</div>
		<button type="submit">Book The Rooms</button>
	</form>
</div>

<Modal title="Edit your details" open={showModal} on:close={() => handleToggleModal()}>
	<svelte:fragment slot="body">{modalContent}</svelte:fragment>
</Modal>

<style>
	body {
		width: 500px;
		margin: 0 auto;
		padding: 50px;
	}

	div.elem-group {
		margin: 20px 0;
	}

	div.elem-group.inlined {
		width: 49%;
		display: inline-block;
		float: left;
		margin-left: 1%;
	}

	label {
		display: block;
		font-family: 'Nanum Gothic';
		padding-bottom: 10px;
		font-size: 1.25em;
	}

	input,
	select,
	textarea {
		border-radius: 2px;
		border: 2px solid #777;
		box-sizing: border-box;
		font-size: 1.25em;
		font-family: 'Nanum Gothic';
		width: 100%;
		padding: 10px;
	}

	div.elem-group.inlined input {
		width: 95%;
		display: inline-block;
	}

	textarea {
		height: 250px;
	}

	hr {
		border: 1px dotted #ccc;
	}

	button {
		height: 50px;
		background: purple;
		border: none;
		color: white;
		font-size: 1.25em;
		font-family: 'Nanum Gothic';
		border-radius: 4px;
		cursor: pointer;
		padding: 12.5px;
	}

	button:hover {
		border: 2px solid black;
	}

	@import url('https://fonts.googleapis.com/css?family=Open+Sans|Playfair+Display+SC');

	* {
		margin: 0;
		padding: 0;
	}

	a {
		text-decoration: none;
		color: inherit;
	}

	body {
		font: normal 18px 'Open Sans', sans-serif;
		background: #fafafa;
		color: #333;
	}

	main {
		min-height: 100vh;
	}

	header {
		background: white;
		box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
	}
	h1 {
		font: normal 4em 'Playfair Display SC', serif;
		text-align: center;
	}

	nav {
		max-width: 800px;
		margin: auto;
		display: flex;
		flex-wrap: wrap;
	}

	nav a {
		flex-grow: 1;
		text-align: center;
		padding: 1em;
		position: relative;
	}

	nav a::after {
		content: '';
		position: absolute;
		bottom: 0;
		left: 0;
		right: 0;
		height: 2px;
		transform: scaleX(0);
		background: #333;
		transition: 0.7s transform cubic-bezier(0.06, 0.9, 0.28, 1);
	}

	nav a:hover::after {
		transform: scaleX(1);
	}

	/* styles for the divider */
	.divider {
		height: 1px;
		background-color: #ccc;
		margin: 20px 0;
	}

	/* media queries for mobile devices */
	@media only screen and (max-width: 600px) {
		body {
			width: 100%;
			padding: 0;
		}

		header {
			padding: 10px;
		}

		h1 {
			font-size: 2em;
		}

		nav {
			flex-direction: column;
			align-items: center;
		}

		nav a {
			padding: 0.5em;
		}

		.divider {
			margin: 10px 0;
		}
	}
</style>
