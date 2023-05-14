<script lang="ts">
	import Search from '$lib/Search.svelte';

	function handleSearch(query: string) {
		console.log(query);
	}
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
	<div class="w-full mt-4">
		<Search onSearch={handleSearch} />
	</div>
</div>
