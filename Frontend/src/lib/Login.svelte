<script lang="ts">
	// import Modal from 'svelte-pieces/ui/Modal.svelte';
	// import { FirebaseUiAuth, saveUserData } from 'sveltefirets';
	import { createEventDispatcher, onMount } from 'svelte';
	import { redirect } from '@sveltejs/kit';
	import { goto } from '$app/navigation';
	import { auth } from '$lib/firebase';
	import { userStore } from 'sveltefire';
	import { signInWithPopup } from 'firebase/auth';
	import { GoogleAuthProvider } from 'firebase/auth';
	import TokenMenu from './TokenMenu.svelte';
	const user = userStore(auth);
	// get user token from subscription to userStore
	let userToken = '';
	user.subscribe((u) => {
		if (u) {
			u.getIdToken().then((t) => (userToken = t));
		}
	});

	let isDev = import.meta.env.DEV;
</script>

{#if $user}
	{#if isDev}
		<TokenMenu />
	{/if}
	<!-- button follow the site style -->
	<!-- center -->
	<div class="flex justify-center items-center flex-col mt-8">
		<button
			class="px-8 py-4 text-lg font-medium text-gray-800 bg-gray-200 border-2 border-black rounded-md hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500"
			on:click={() => goto('/book')}
		>
			<b>Book a room</b>
		</button>
	</div>
{:else}
	<button
		class="px-4 py-2 text-lg font-medium text-gray-800 bg-gray-200 border-2 border-black rounded-md hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500"
		on:click={() => signInWithPopup(auth, new GoogleAuthProvider())}
	>
		<div class="flex items-center">
			<img
				class="w-6 h-6 mr-3"
				src="https://upload.wikimedia.org/wikipedia/commons/5/53/Google_%22G%22_Logo.svg"
				alt="Google logo"
			/>
			<span>Login with Google</span>
		</div>
	</button>
{/if}
