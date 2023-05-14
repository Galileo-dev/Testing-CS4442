<script lang="ts">
	// import Modal from 'svelte-pieces/ui/Modal.svelte';
	import { FirebaseUiAuth, saveUserData } from 'sveltefirets';
	import { createEventDispatcher, onMount } from 'svelte';
	import { redirect } from '@sveltejs/kit';
	import { goto } from '$app/navigation';

	let token: string;

	let copied = false;

	function copyToken() {
		navigator.clipboard.writeText(token);
		copied = true;
	}

	onMount(() => {
		setTimeout(() => {
			copied = false;
		}, 3000);
	});

	const handleAuthResult = (event: CustomEvent) => {
		// Save user data and token
		goto('/book');
	};
</script>

<!-- <button
	class="px-4 py-2 text-lg font-medium text-gray-800 bg-gray-200 border-2 border-black rounded-md hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500"
>
	<div class="flex items-center">
		<img
			class="w-6 h-6 mr-3"
			src="https://upload.wikimedia.org/wikipedia/commons/5/53/Google_%22G%22_Logo.svg"
			alt="Google logo"
		/>
		<span>Login with Google</span>
	</div>
</button> -->
<!-- align center -->
<div class="mx-auto max-w-lg md:max-w-xl lg:max-w-4xl">
	<div class="bg-white rounded-lg shadow-lg p-6 overflow-hidden">
		<p class="text-center mb-4 truncate">Token: {token}</p>
		<div class="flex justify-center items-center">
			<button
				class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded w-full md:w-auto"
				on:click={copyToken}
				style="min-width: 8rem;"
			>
				{copied ? 'Copied!' : 'Copy Token'}
			</button>
		</div>
	</div>
</div>

<FirebaseUiAuth
	signInWith={{ google: true, emailPassword: false }}
	on:authresult={(e) => {
		saveUserData(e.detail);
		e.detail.user?.getIdToken().then((t) => (token = t));
	}}
	on:success={handleAuthResult}
/>
