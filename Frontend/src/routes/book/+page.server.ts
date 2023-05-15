import type { PageServerLoad } from './$types';

interface Room {
	id: number;
	displayName: string;
	isAvailable: boolean;
}

export const load = (async ({ fetch, params }) => {
	const res = await fetch(`/api/rooms`);
	const rooms = await res.json();

	return {
		rooms: rooms as Room[]
	};
}) satisfies PageServerLoad;
