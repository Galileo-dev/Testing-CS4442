<script>
	import Login from '$lib/Login.svelte';
</script>

<div class="flex items-center justify-center h-screen">
	<div class="mx-auto">
		<!-- card that contains the comming soon text -->
		<div class="bg-white rounded-lg shadow-lg p-6 overflow-hidden">
			<p class="text-center mb-4 truncate text-4xl">Coming Soonest</p>
		</div>
	</div>
</div>

<style lang="postcss">
	:global(html) {
		background-color: theme(colors.gray.100);
	}
</style>
