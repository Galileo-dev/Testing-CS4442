<script lang="ts">
	import Booking from './traditionalBookingView.svelte';
	import Search from '$lib/Search.svelte';
	import SearchView from './gptBookingView.svelte';
	import type { PageData } from './$types';
	export let data: PageData;
	let bookingNew = true;
</script>

<div class="flex flex-col items-center">
	<!-- button to toggle tailwind -->
	<button
		class="absolute bottom-0 right-0 px-2 py-1 text-sm font-medium text-gray-800 bg-gray-200 border-2 border-black rounded-md hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500"
		on:click={() => (bookingNew = !bookingNew)}
	>
		Toggle Booking
	</button>

	<!-- if else -->
	{#if bookingNew}
		<Booking {data} />
	{:else}
		<SearchView />
	{/if}
</div>
