DROP TABLE IF EXISTS public.user;

CREATE TABLE public.user (
	id SERIAL PRIMARY KEY NOT NULL,
	username character varying NOT NULL,
	email character varying NOT NULL,
	firstname character varying NOT NULL,
	jumpcloud_id character varying NOT NULL

);