<script>
	import Login from '$lib/Login.svelte';
</script>

<div class="flex items-center justify-center h-screen">
	<div class="mx-auto">
		<Login />
	</div>
</div>

<style lang="postcss">
	:global(html) {
		background-color: theme(colors.gray.100);
	}
</style>
