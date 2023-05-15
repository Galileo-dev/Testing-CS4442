<script lang="ts">
	import Search from '$lib/Search.svelte';

	import { auth } from '$lib/firebase';
	import { userStore } from 'sveltefire';
	import { onMount } from 'svelte';
	import type { PageData } from './$types';
	import Modal from '$lib/Modal.svelte';

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
	let room_preference: string = rooms[0].id.toString();
	let lengthofstay: string = '';

	const handleRoomSelection = (e: Event) => {
		let target = e.target as HTMLInputElement;
		room_preference = target.value;
		console.log(room_preference);
	};

	const handleLengthSelection = (e: Event) => {
		let target = e.target as HTMLInputElement;
		lengthofstay = target.value;
		console.log(lengthofstay);
	};

	interface SearchEventDetail {
		query: string;
	}

	const handleSearch = async (e: CustomEvent<SearchEventDetail>) => {
		let body = {
			room_id: room_preference,
			unparsed_date_time: e.detail,
			length_in_mins: lengthofstay
		};

		console.log(body);

		const res = await fetch('http://127.0.0.1:8000/add_booking/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${userToken}`
			},
			body: JSON.stringify(body)
		});
		const json = await res.json();
		console.log(json);
		modalContent = json.message;
		showModal = true;
	};
</script>

<div class="flex flex-col items-center w-full">
	<div class="w-full mt-8 mb-8">
		<h1 class="text-center text-4xl font-bold text-gray-800 mb-2">
			(<s><em>BookMe</em></s>) GPT Booking
		</h1>
		<p class="text-center text-lg">
			use <b>natural</b> text to get a list of <em>available bookings&trade;</em>
		</p>
	</div>

	<div class="p-4 flex items-center">
		<label for="room-selection" class="font-medium text-gray-700 mr-4">Select Room to Book:</label>
		<div class="relative">
			<select
				id="room-selection"
				name="	"
				required
				class="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline"
				on:change={handleRoomSelection}
				bind:value={room_preference}
			>
				{#each rooms as room}
					<option value={room.id}>{room.displayName}</option>
				{/each}
			</select>
			<div
				class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700"
			/>
		</div>
	</div>
	<div class="p-4 flex items-center">
		<label for="room-selection" class="font-medium text-gray-700 mr-4"
			>Length of Stay (minutes)</label
		>
		<div class="relative">
			<input
				type="number"
				id="length-of-stay"
				name="lengthofstay"
				placeholder="60"
				min="0"
				required
				class="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline"
				on:change={handleLengthSelection}
				bind:value={lengthofstay}
			/>
			<div
				class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700"
			/>
		</div>
	</div>
	<div class="w-full mt-4">
		<Search
			on:submit={handleSearch}
			label="Book time"
			placeholder="The eleventh of november at ten o'clock"
		/>
	</div>
</div>

<Modal title="Edit your details" open={showModal} on:close={() => handleToggleModal()}>
	<svelte:fragment slot="body">{modalContent}</svelte:fragment>
</Modal>
