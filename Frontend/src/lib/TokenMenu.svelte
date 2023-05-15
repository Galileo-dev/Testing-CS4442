<script lang="ts">
	import { userStore } from 'sveltefire';
	import { auth } from '$lib/firebase';
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
		setTimeout(() => {
			copied = false;
		}, 3000);
	}
</script>

{#if $user}
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
