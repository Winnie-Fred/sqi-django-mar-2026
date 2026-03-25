// ── BOOKVERSE APP.JS ──
// Shared state, data, and utilities

// ── SEED DATA ──
const SEED_BOOKS = [
  {
    id: "b1",
    title: "Dune",
    author: "Frank Herbert",
    genre: "Sci-Fi",
    year: 1965,
    cover: "https://images.unsplash.com/photo-1614728894747-a83421e2b9c9?w=400&q=80",
    description: "Set in the distant future amidst a feudal interstellar society, Dune tells the story of young Paul Atreides, whose family accepts the stewardship of the desert planet Arrakis. As the only producer of the most valuable substance in the universe, control of Arrakis is highly contested among the noble houses of the Imperium.",
    pages: 688,
    isbn: "978-0441013593"
  },
  {
    id: "b2",
    title: "The Silent Patient",
    author: "Alex Michaelides",
    genre: "Mystery",
    year: 2019,
    cover: "https://images.unsplash.com/photo-1512820790803-83ca734da794?w=400&q=80",
    description: "Alicia Berenson's life is seemingly perfect — a famous painter married to an in-demand fashion photographer. She's living everyone's dream in a grand house in London's most desirable neighbourhood. One evening her husband Gabriel returns home late from a fashion shoot, and Alicia shoots him five times in the face, and then never speaks another word.",
    pages: 336,
    isbn: "978-1250301697"
  },
  {
    id: "b3",
    title: "The Hitchhiker's Guide to the Galaxy",
    author: "Douglas Adams",
    genre: "Sci-Fi",
    year: 1979,
    cover: "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=400&q=80",
    description: "Seconds before Earth is demolished to make way for a hyperspatial express route, Arthur Dent is plucked off the planet by his friend Ford Prefect, a researcher for the revised edition of the titular encyclopaedia. Together this raggedy band must conquer not just one but several wildly impossible circumstances.",
    pages: 224,
    isbn: "978-0345391803"
  },
  {
    id: "b4",
    title: "It",
    author: "Stephen King",
    genre: "Horror",
    year: 1986,
    cover: "https://images.unsplash.com/photo-1504701954957-2010ec3bcec1?w=400&q=80",
    description: "Welcome to Derry, Maine. It's a small city, a nice place to raise a kid. But in Derry a deeply frightening evil lurks beneath the surface — a shapeshifting monster that can be anything: a clown, a mummy, a werewolf, a spider. For the children of the Losers Club, the nightmare is real.",
    pages: 1138,
    isbn: "978-1501156700"
  },
  {
    id: "b5",
    title: "Gone Girl",
    author: "Gillian Flynn",
    genre: "Thriller",
    year: 2012,
    cover: "https://images.unsplash.com/photo-1495640452828-3df6795cf69b?w=400&q=80",
    description: "On the morning of their fifth wedding anniversary, Nick Dunne's wife Amy mysteriously disappears. Unraveling the clues left behind by Amy, Nick becomes entangled in a media circus while questions mount about his involvement in her disappearance.",
    pages: 422,
    isbn: "978-0307588364"
  },
  {
    id: "b6",
    title: "The Name of the Wind",
    author: "Patrick Rothfuss",
    genre: "Fantasy",
    year: 2007,
    cover: "https://images.unsplash.com/photo-1518770660439-4636190af475?w=400&q=80",
    description: "Told in Kvothe's own words, this is the tale of the magically gifted young man who grows to be the most notorious wizard his world has ever seen. The intimate narrative of his childhood in a troupe of traveling players, his years spent as a near-feral orphan in a crime-ridden city, his daringly brazen yet successful gamble to enter a legendary school of magic.",
    pages: 662,
    isbn: "978-0756404079"
  },
  {
    id: "b7",
    title: "Neuromancer",
    author: "William Gibson",
    genre: "Sci-Fi",
    year: 1984,
    cover: "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=400&q=80",
    description: "Case was the sharpest data-thief in the matrix — until he crossed the wrong people and they crippled his nervous system, banishing him from cyberspace. Now a mysterious new employer has recruited him for a last-chance run at an unthinkably powerful artificial intelligence.",
    pages: 271,
    isbn: "978-0441569595"
  },
  {
    id: "b8",
    title: "The Shining",
    author: "Stephen King",
    genre: "Horror",
    year: 1977,
    cover: "https://images.unsplash.com/photo-1487700160041-babef9c3cb55?w=400&q=80",
    description: "Jack Torrance's new job at the Overlook Hotel is the perfect chance for a fresh start. As the off-season caretaker at the atmospheric old hotel, he'll have plenty of time to spend reconnecting with his family and working on his writing. But as the harsh winter weather sets in, the idyllic location feels ever more remote — and haunted.",
    pages: 447,
    isbn: "978-0307743657"
  },
  {
    id: "b9",
    title: "Project Hail Mary",
    author: "Andy Weir",
    genre: "Sci-Fi",
    year: 2021,
    cover: "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?w=400&q=80",
    description: "Ryland Grace is the sole survivor on a desperate, last-chance mission — and if he fails, humanity and the Earth itself will perish. Except he doesn't know that. He can't even remember his own name, let alone the nature of his assignment or how to complete it.",
    pages: 476,
    isbn: "978-0593135204"
  },
  {
    id: "b10",
    title: "Normal People",
    author: "Sally Rooney",
    genre: "Literary Fiction",
    year: 2018,
    cover: "https://images.unsplash.com/photo-1474932430478-367dbb6832c1?w=400&q=80",
    description: "Connell and Marianne grew up in the same small town, but the similarities end there. At school, Connell is popular and well-liked, while Marianne is a loner. But when the two strike up a conversation — and then a relationship — the true story of their connection is far more complicated.",
    pages: 273,
    isbn: "978-0571334650"
  },
  {
    id: "b11",
    title: "The Midnight Library",
    author: "Matt Haig",
    genre: "Literary Fiction",
    year: 2020,
    cover: "https://images.unsplash.com/photo-1532012197267-da84d127e765?w=400&q=80",
    description: "Between life and death there is a library, and within that library, the shelves go on forever. Every book provides a chance to try another life you could have lived. To see how things would be if you had made other choices. Would you have done anything different, if you had the chance to undo your regrets?",
    pages: 288,
    isbn: "978-0525559474"
  },
  {
    id: "b12",
    title: "Educated",
    author: "Tara Westover",
    genre: "Biography",
    year: 2018,
    cover: "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=400&q=80",
    description: "Tara Westover was seventeen the first time she set foot in a classroom. Born to survivalists in the mountains of Idaho, she prepared for the end of the world by stockpiling canned peaches and sleeping with her head under her mattress. She had no birth certificate. She had no medical records. There was no proof she existed.",
    pages: 352,
    isbn: "978-0399590504"
  }
];

// ── STORAGE HELPERS ──
function getBooks() {
  const stored = localStorage.getItem('bv_books');
  if (!stored) {
    localStorage.setItem('bv_books', JSON.stringify(SEED_BOOKS));
    return SEED_BOOKS;
  }
  return JSON.parse(stored);
}

function getBookById(id) {
  return getBooks().find(b => b.id === id) || null;
}

function getReviews() {
  const stored = localStorage.getItem('bv_reviews');
  return stored ? JSON.parse(stored) : [];
}

function saveReviews(reviews) {
  localStorage.setItem('bv_reviews', JSON.stringify(reviews));
}

function getReviewsForBook(bookId) {
  return getReviews().filter(r => r.bookId === bookId);
}

function getReviewById(reviewId) {
  return getReviews().find(r => r.id === reviewId) || null;
}

function addReview(review) {
  const reviews = getReviews();
  reviews.push(review);
  saveReviews(reviews);
}

function updateReview(reviewId, updates) {
  const reviews = getReviews();
  const idx = reviews.findIndex(r => r.id === reviewId);
  if (idx !== -1) {
    reviews[idx] = { ...reviews[idx], ...updates };
    saveReviews(reviews);
    return reviews[idx];
  }
  return null;
}

function deleteReview(reviewId) {
  const reviews = getReviews().filter(r => r.id !== reviewId);
  saveReviews(reviews);
}

// ── AUTH HELPERS ──
function getUsers() {
  const stored = localStorage.getItem('bv_users');
  return stored ? JSON.parse(stored) : [];
}

function saveUsers(users) {
  localStorage.setItem('bv_users', JSON.stringify(users));
}

function getCurrentUser() {
  const stored = sessionStorage.getItem('bv_current_user');
  return stored ? JSON.parse(stored) : null;
}

function setCurrentUser(user) {
  if (user) {
    sessionStorage.setItem('bv_current_user', JSON.stringify(user));
  } else {
    sessionStorage.removeItem('bv_current_user');
  }
}

function registerUser(name, email, password) {
  const users = getUsers();
  if (users.find(u => u.email === email)) {
    return { success: false, error: 'Email already registered.' };
  }
  const user = {
    id: 'u' + Date.now(),
    name,
    email,
    password, // In production: hash this!
    createdAt: new Date().toISOString()
  };
  users.push(user);
  saveUsers(users);
  return { success: true, user };
}

function loginUser(email, password) {
  const users = getUsers();
  const user = users.find(u => u.email === email && u.password === password);
  if (!user) return { success: false, error: 'Invalid email or password.' };
  const { password: _, ...safeUser } = user;
  setCurrentUser(safeUser);
  return { success: true, user: safeUser };
}

function logoutUser() {
  setCurrentUser(null);
}

// ── RATING HELPERS ──
function getAverageRating(bookId) {
  const reviews = getReviewsForBook(bookId);
  if (!reviews.length) return 0;
  return reviews.reduce((sum, r) => sum + r.rating, 0) / reviews.length;
}

function renderStars(rating, maxStars = 5) {
  let html = '<span class="stars">';
  for (let i = 1; i <= maxStars; i++) {
    if (i <= Math.floor(rating)) {
      html += '<span class="star">★</span>';
    } else if (i - 0.5 <= rating) {
      html += '<span class="star" style="opacity:0.6">★</span>';
    } else {
      html += '<span class="star star-empty">★</span>';
    }
  }
  html += '</span>';
  return html;
}

// ── URL PARAMS ──
function getParam(key) {
  return new URLSearchParams(window.location.search).get(key);
}

// ── DATE FORMAT ──
function formatDate(isoStr) {
  const d = new Date(isoStr);
  return d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
}

// ── AVATAR INITIAL ──
function getInitial(name) {
  return (name || '?')[0].toUpperCase();
}

// ── TOAST ──
function showToast(message, type = 'info', duration = 3500) {
  let container = document.querySelector('.toast-container');
  if (!container) {
    container = document.createElement('div');
    container.className = 'toast-container';
    document.body.appendChild(container);
  }
  const icons = { success: '✓', error: '✕', info: 'ℹ' };
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.innerHTML = `<span style="font-size:1rem">${icons[type]}</span> ${message}`;
  container.appendChild(toast);
  setTimeout(() => {
    toast.style.animation = 'toastOut 0.3s ease forwards';
    setTimeout(() => toast.remove(), 300);
  }, duration);
}

// ── GENERATE ID ──
function genId() {
  return 'r' + Date.now() + Math.random().toString(36).slice(2, 7);
}

// ── INIT NAV ──
function initNav(activePage) {
  const user = getCurrentUser();
  const actionsEl = document.getElementById('nav-actions');
  if (!actionsEl) return;

  if (user) {
    actionsEl.innerHTML = `
      <span class="nav-user-name">Hi, ${user.name.split(' ')[0]}</span>
      <button class="btn btn-outline" onclick="handleLogout()">Log Out</button>
    `;
  } else {
    actionsEl.innerHTML = `
      <a href="login.html" class="btn btn-ghost">Log In</a>
      <a href="register.html" class="btn btn-primary">Sign Up</a>
    `;
  }

  // Set active nav link
  document.querySelectorAll('.nav-links a').forEach(a => {
    a.classList.remove('active');
    if (a.dataset.page === activePage) a.classList.add('active');
  });
}

function handleLogout() {
  logoutUser();
  showToast('Logged out successfully', 'info');
  setTimeout(() => window.location.href = 'index.html', 600);
}

// ── REQUIRE AUTH ──
function requireAuth(redirectBack) {
  const user = getCurrentUser();
  if (!user) {
    const url = redirectBack ? `login.html?next=${encodeURIComponent(redirectBack)}` : 'login.html';
    window.location.href = url;
    return null;
  }
  return user;
}
