import type { RequestHandler } from '@sveltejs/kit';
import { env } from '$env/dynamic/private';

export const GET: RequestHandler = async ({ url, request, fetch }) => {
	try {
		return await fetch(`${env.API_URL}/${url.pathname}`, {
			...request
		});
	} catch (err: unknown) {
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
	try {
		return await fetch(`http://127.0.0.1:5000${url.pathname}`, {
			...request,
			body: await request.text(),
			method: 'POST',
			headers: new Headers({
				'Content-Type': 'application/json'
			})
		});
	} catch (err: unknown) {
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
