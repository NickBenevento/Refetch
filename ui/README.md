# UI Documentation

## Setting up the project
`npm create vite@latest <project-name> -- --template react`

VITE + Tailwind Setup:
https://tailwindcss.com/docs/installation/using-vite

# Package / Library Notes

- Vite
- Typescript + React
- TailwindCSS
- Ky
- Jotai
- TanStack Query
- Query Key Factory

## [ky](https://github.com/sindresorhus/ky)
Small, elegant, built on top of built-in "fetch"
- simpler API, method shortcuts
- retries requests
- timeout capability


## [Jotai](https://jotai.org/)
Jotai is used for client-side state management. Think useState, but better:
- light, less boilerplate --> don't need actions / reducers
- Can be used outside of components
- Performance --> reduces re-renders
- Can easily be split to read / write from different components

## _TODO [TanStack Query](https://tanstack.com/query/latest)_
Used for server-side state management (e.g. API data)
- Set queries so that they can be invalidated + automatically refreshed when data changes

### _TODO [Query Key Factory](https://github.com/lukemorales/query-key-factory)_


# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh
