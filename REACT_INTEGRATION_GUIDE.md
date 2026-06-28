# React & shadcn/ui Integration Guide

This guide details how to integrate and run the newly added React components (`saa-s-template.tsx` and `demo.tsx`) inside the Django-based application environment.

## 1. Project Prerequisites

To support React, TypeScript, and Tailwind CSS, you should initialize a Node.js frontend workspace. There are two primary integration methods:
- **Option A (Recommended for standard deployments):** Run a standalone React frontend (e.g. Next.js or Vite) that communicates with Django via REST APIs or GraphQL.
- **Option B (Monorepo / Hybrid):** Build the React components into static bundles using Vite/Webpack and serve them directly via Django's static files.

Below, we detail how to set up a standard standalone Vite + React + TypeScript + Tailwind workspace that uses the shadcn project structure.

### Step 1.1: Initialize a Vite + React + TypeScript Project
In your terminal, run:
```bash
# Create a new Vite React app in a frontend subdirectory (e.g., 'frontend')
npm create vite@latest frontend -- --template react-ts
cd frontend
npm install
```

### Step 1.2: Install and Configure Tailwind CSS
Tailwind CSS is required for styling the integrated components.
1. Install Tailwind CSS and its peer dependencies:
   ```bash
   npm install -D tailwindcss postcss autoprefixer
   npx tailwindcss init -p
   ```
2. Configure your `tailwind.config.js` to search for components:
   ```javascript
   /** @type {import('tailwindcss').Config} */
   export default {
     content: [
       "./index.html",
       "./src/**/*.{js,ts,jsx,tsx}",
     ],
     theme: {
       extend: {},
     },
     plugins: [],
   }
   ```
3. Add the Tailwind directives to your main CSS file (e.g., `./src/index.css`):
   ```css
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   ```

### Step 1.3: Initialize shadcn/ui via CLI
shadcn/ui provides beautifully designed components that you copy and paste into your project.
1. Run the shadcn CLI initialization command inside your frontend directory:
   ```bash
   npx shadcn-ui@latest init
   ```
2. During initialization, you will be prompted with setup questions. Recommended options:
   - **Style:** Default
   - **Base color:** Slate or Zinc
   - **CSS variables:** Yes
   - **Configure import aliases:** Yes (e.g., `@/*` for src and `@/components/*` for components)

---

## 2. Default Path for Components and Styles

### Why is `/components/ui` important?
In the shadcn project structure, the default path for reusable UI components is `/components/ui`.
- **Namespace Separation:** It cleanly separates your primary application code, layouts, and pages from low-level reusable primitives (buttons, inputs, dialogs).
- **Import Alias Compatibility:** It integrates with standard import aliases (e.g., `import { Button } from "@/components/ui/button"`). This prevents deep, fragile relative imports (like `../../../components/ui/button`).
- **CLI Automation:** When running shadcn CLI commands to add components (e.g., `npx shadcn-ui@latest add button`), the CLI automatically installs them in `/components/ui`. Keeping your components here ensures the CLI works seamlessly without breaking imports.

---

## 3. Serving the React Components inside Django

To bridge the gap between Django and React:
1. **API Integration:** Configure your Django views in `bank_app/views.py` to return JSON data (using Django Rest Framework or standard `JsonResponse`).
2. **Build and Serve:**
   - In React, run: `npm run build`
   - Copy the build output (`dist/assets/*` and `dist/index.html`) to Django's `static/` and `templates/` folders.
   - Configure Django settings to point to the built static bundle.
