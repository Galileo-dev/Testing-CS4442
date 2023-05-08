<script lang="ts">
	let messages: any = [];
	let newMessage = '';

	function sendMessage() {
		messages = [...messages, newMessage];
		newMessage = '';
		scrollToBottom();
	}

	function scrollToBottom() {
		const chatMessages: any = document.getElementById('chat-messages');
		chatMessages.scrollTop = chatMessages.scrollHeight;
	}
</script>

<!-- make it 800px * 500px -->
<div class="flex items-center justify-center">
	<div class="w-full md:w-1/2 lg:w-1/3 xl:w-1/4">
		<div class="h-screen sm:h-3/4 md:h-1/2 lg:h-1/3 xl:h-1/4">
			<div class="h-screen flex flex-col justify-between bg-white rounded-lg shadow-lg">
				<div class="flex-grow flex flex-col px-4 py-8 overflow-y-auto">
					{#each messages as message}
						<div class="mb-4 p-2 rounded-lg max-w-lg self-start bg-gray-100">
							<p class="text-sm">{message}</p>
						</div>
					{/each}
				</div>

				<div class="flex items-center justify-center p-4">
					<input
						class="w-full px-4 py-2 rounded-full bg-gray-100 focus:outline-none"
						type="text"
						placeholder="Type a message..."
						bind:value={newMessage}
						on:keydown={(event) => {
							if (event.key === 'Enter') sendMessage();
						}}
					/>

					<button
						class="ml-2 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-full"
						on:click={sendMessage}
					>
						Send
					</button>
				</div>
			</div>
		</div>
	</div>
</div>
