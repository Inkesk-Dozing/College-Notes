# Comprehensive React Routing Guide (React Router v6 & v7)

## 1. Core Concepts: SPA vs Traditional Routing
Before diving into code, it's important to understand *why* we use React Router.

| Feature | Traditional Routing (MPA) | Client-Side Routing (SPA) |
| :--- | :--- | :--- |
| **Request** | Browser requests a new HTML file from the server. | Browser intercept the request; React updates the DOM locally. |
| **Reload** | Full page refresh (white flash). | No page reload; seamless transition. |
| **State** | Lost on every navigation. | Maintained across "pages". |
| **Speed** | Slower (server latency). | Instant (after initial bundle load). |

---

## 2. Installation & Basic Setup
Install the official library:
```bash
npm install react-router-dom
```

### The "Big Three" Components
1. **`<BrowserRouter>`**: The top-level provider that connects your app to the browser's URL. Usually wraps your entire `<App />`.
2. **`<Routes>`**: The container that looks at the current URL and decides which child `Route` to show.
3. **`<Route />`**: The mapping between a URL `path` and a React `element`.

```jsx
// src/main.jsx
import { BrowserRouter } from "react-router-dom";

ReactDOM.createRoot(document.getElementById("root")).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
```

---

## 3. Navigation: Moving Between Pages
Never use `<a href="...">` for internal links. It triggers a refresh, defeating the purpose of an SPA.

### A. The `<Link>` Component
Basic navigation without refresh.
```jsx
import { Link } from "react-router-dom";

<Link to="/about">Go to About</Link>
```

### B. The `<NavLink>` Component
Special version of `Link` that knows if it is "active". Great for navigation bars.
```jsx
<NavLink 
  to="/services"
  style={({ isActive }) => ({ color: isActive ? "red" : "black" })}
>
  Services
</NavLink>
```

---

## 4. Advanced Hook-Based Navigation

### A. `useNavigate` (Programmatic)
Used to redirect users via code (e.g., after a login or timer).
```jsx
const navigate = useNavigate();

const logout = () => {
  localStorage.clear();
  navigate("/login", { replace: true }); // 'replace' removes the current page from history
};
```

### B. `useLocation`
Returns the current location object. Useful for tracking page views or reading state passed via a link.
```jsx
const location = useLocation();
console.log(location.pathname); // e.g., "/about"
```

### C. Passing State via Links
You can pass data to a route without showing it in the URL.
```jsx
// Passing
<Link to="/details" state={{ from: "homepage", id: 123 }}>View</Link>

// Receiving
const location = useLocation();
const { from, id } = location.state || {};
```

---

## 5. Dynamic Routing & Search Params

### A. URL Parameters (`useParams`)
Defining placeholders in routes.
```jsx
// Route Definition
<Route path="/product/:sku" element={<ProductDetail />} />

// Component Access
const { sku } = useParams();
```

### B. Search/Query Parameters (`useSearchParams`)
Handling `?query=react&sort=asc`.
```jsx
const [searchParams, setSearchParams] = useSearchParams();
const query = searchParams.get("query");

// Updating URL params without navigation
const updateQuery = () => setSearchParams({ query: "javascript" });
```

---

## 6. Layouts & Nested Routing
Use nested routes to share a layout (header/footer/sidebar) across multiple sub-pages.

```jsx
<Routes>
  <Route path="/" element={<MainLayout />}>
    <Route index element={<Home />} /> {/* Renders at / */}
    <Route path="profile" element={<Profile />} /> {/* Renders at /profile */}
    <Route path="settings" element={<Settings />} /> {/* Renders at /settings */}
  </Route>
</Routes>
```

### The `<Outlet />`
In your `MainLayout` component, you MUST use `<Outlet />` to specify where the child routes should be injected.
```jsx
import { Outlet } from "react-router-dom";

function MainLayout() {
  return (
    <div>
      <Navbar />
      <main>
        <Outlet /> {/* Child components go here! */}
      </main>
      <Footer />
    </div>
  );
}
```

---

## 7. Protected Routes (Authentication)
A common pattern to prevent unauthorized access to specific pages.

```jsx
const ProtectedRoute = ({ children }) => {
  const isAuthenticated = !!localStorage.getItem("token");
  return isAuthenticated ? children : <Navigate to="/login" />;
};

// Usage
<Route path="/dashboard" element={
  <ProtectedRoute>
    <Dashboard />
  </ProtectedRoute>
} />
```

---

## 8. Performance: Lazy Loading
For large apps, don't load all pages at once. Load them only when the user navigates there.

```jsx
import { lazy, Suspense } from "react";

const AdminPanel = lazy(() => import("./pages/AdminPanel"));

function App() {
  return (
    <Suspense fallback={<div>Loading Page...</div>}>
      <Routes>
        <Route path="/admin" element={<AdminPanel />} />
      </Routes>
    </Suspense>
  );
}
```

---

## 9. Handling 404 (Wildcard Route)
Always include a fallback route at the very bottom of your `<Routes>`.

```jsx
<Route path="*" element={<NotFoundPage />} />
```

---

## 10. React Router v7: The Future (Data APIs)
React Router v7 (and late v6) introduced "Data APIs" (Loaders and Actions), which follow the Remix philosophy of moving data fetching into the router logic.

- **Loaders**: Fetch data *before* the component renders.
- **Actions**: Handle form submissions/mutations.
- **CreateBrowserRouter**: The modern way to define routes using objects instead of JSX.

```jsx
// Modern Object Approach
const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    loader: async () => fetch("/api/user"),
    children: [ ... ]
  }
]);
```

---

## Vocabulary Recap
- **Slug**: The dynamic part of a URL (e.g., in `/post/my-first-blog`, `my-first-blog` is the slug).
- **Index Route**: The default child route of a parent.
- **Wildcard (`*`)**: Matches anything.
- **Outlet**: Placeholder for nested UI.
- **Programmatic Nav**: Navigating via logic instead of a user click.
