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
	const user = userStore(auth);
	// get user token from subscription to userStore
	let userToken = '';
	user.subscribe((u) => {
		if (u) {
			u.getIdToken().then((t) => (userToken = t));
		}
	});

	let isDev = import.meta.env.DEV;

	let loggedIn = false;
	let copied = false;

	function copyToken() {
		navigator.clipboard.writeText(userToken);
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

{#if $user}
	{#if isDev}
		<!-- align center -->
		<div class="mx-auto max-w-lg md:max-w-xl lg:max-w-4xl">
			<div class="bg-white rounded-lg shadow-lg p-6 overflow-hidden">
				<p class="text-center mb-4 truncate">Token: {userToken}</p>
				<div class="flex justify-center items-center flex-col">
					<button
						class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded w-full md:w-auto mb-4"
						style="min-width: 8rem;"
						on:click={copyToken}
					>
						{copied ? 'Copied!' : 'Copy Token'}
					</button>
					<button
						class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded w-full md:w-auto"
						style="min-width: 8rem;"
						on:click={() => auth.signOut()}
					>
						Sign Out
					</button>
				</div>
			</div>
		</div>
	{/if}
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
