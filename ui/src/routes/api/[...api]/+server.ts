import type { RequestHandler } from '@sveltejs/kit';
import { env } from '$env/dynamic/private';

export const GET: RequestHandler = async ({ url, request, fetch }) => {
	try {
		return await fetch(`${env.API_URL}/${url.pathname.replace('/api/', '')}`, {
			...request
		});
	} catch (err: unknown) {
		console.debug('Error', err);
		if (err instanceof TypeError && (err.cause as Record<string, string>).code === 'ECONNREFUSED') {
			return new Response(
				JSON.stringify({
					reason: 'Failed to connect to API -- is it running?'
				}),
				{ status: 500 }
			);
		}

		return new Response(JSON.stringify({}), { status: 400 });
	}
};

export const POST: RequestHandler = async ({ url, request, fetch }) => {
	console.debug('Request', request);
	try {
		return await fetch(`${env.API_URL}/${url.pathname.replace('/api/', '')}`, request);
	} catch (err: unknown) {
		console.debug('Error', err);
		if (err instanceof TypeError && (err.cause as Record<string, string>).code === 'ECONNREFUSED') {
			return new Response(
				JSON.stringify({
					reason: 'Failed to connect to API -- is it running?'
				}),
				{ status: 500 }
			);
		}

		return new Response(JSON.stringify({}), {
			status: 400
		});
	}
};
