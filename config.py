"""
KaamSetu - Central configuration
Contains: paths, worker categories, language/translation system, badge rules.
"""

import os

# ---------------------------------------------------------------------------
# PATHS
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "database")
DB_PATH = os.path.join(DB_DIR, "kaamsetu.db")

UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
PROFILE_UPLOAD_DIR = os.path.join(UPLOAD_DIR, "profiles")
CERT_UPLOAD_DIR = os.path.join(UPLOAD_DIR, "certificates")
PROJECT_UPLOAD_DIR = os.path.join(UPLOAD_DIR, "projects")
VIDEO_UPLOAD_DIR = os.path.join(UPLOAD_DIR, "videos")
VERIFICATION_UPLOAD_DIR = os.path.join(UPLOAD_DIR, "verification")

for d in [DB_DIR, PROFILE_UPLOAD_DIR, CERT_UPLOAD_DIR, PROJECT_UPLOAD_DIR,
          VIDEO_UPLOAD_DIR, VERIFICATION_UPLOAD_DIR]:
    os.makedirs(d, exist_ok=True)

# ---------------------------------------------------------------------------
# FILE UPLOAD RULES
# ---------------------------------------------------------------------------
MAX_IMAGE_SIZE_MB = 5
MAX_VIDEO_SIZE_MB = 50
MAX_DOC_SIZE_MB = 8

ALLOWED_IMAGE_TYPES = ["jpg", "jpeg", "png", "webp"]
ALLOWED_DOC_TYPES = ["jpg", "jpeg", "png", "pdf"]
ALLOWED_VIDEO_TYPES = ["mp4", "mov", "webm"]

# ---------------------------------------------------------------------------
# TRUSTED WORKER BADGE RULE (configurable)
# ---------------------------------------------------------------------------
TRUSTED_WORKER_MIN_COMPLETED_PROJECTS = 10
TRUSTED_WORKER_MIN_RATING = 4.0

# ---------------------------------------------------------------------------
# WORKER CATEGORIES (seeded into DB, database-driven afterwards)
# ---------------------------------------------------------------------------
DEFAULT_CATEGORIES = [
    "Electrician", "Plumber", "Carpenter", "Painter", "Mason", "Mechanic",
    "Cleaner", "Driver", "Gardener", "AC Technician", "Welder",
    "Construction Worker", "Tile Worker", "Roofer", "Furniture Worker",
    "Appliance Repair Technician", "Washing Machine Technician",
    "Refrigerator Technician", "CCTV Technician", "Solar Technician",
    "Computer Technician", "Mobile Repair Technician", "Tailor", "Barber",
    "Beautician", "Cook", "Delivery Worker", "Pest Control Worker",
    "Interior Worker", "Glass Worker",
]

# Emoji/icon shown per category (falls back to a generic icon)
CATEGORY_ICONS = {
    "Electrician": "🔌", "Plumber": "🚰", "Carpenter": "🪚", "Painter": "🎨",
    "Mason": "🧱", "Mechanic": "🔧", "Cleaner": "🧹", "Driver": "🚗",
    "Gardener": "🌱", "AC Technician": "❄️", "Welder": "🛠️",
    "Construction Worker": "👷", "Tile Worker": "🔲", "Roofer": "🏠",
    "Furniture Worker": "🪑", "Appliance Repair Technician": "🧰",
    "Washing Machine Technician": "🧺", "Refrigerator Technician": "🧊",
    "CCTV Technician": "📹", "Solar Technician": "☀️",
    "Computer Technician": "💻", "Mobile Repair Technician": "📱",
    "Tailor": "🧵", "Barber": "💈", "Beautician": "💄", "Cook": "🍳",
    "Delivery Worker": "📦", "Pest Control Worker": "🐜",
    "Interior Worker": "🛋️", "Glass Worker": "🪟",
}
DEFAULT_ICON = "🛠️"

# ---------------------------------------------------------------------------
# LANGUAGES
# ---------------------------------------------------------------------------
LANGUAGES = {
    "English": "en",
    "తెలుగు": "te",
    "हिन्दी": "hi",
}

# Central translation dictionary. Keys are used across the whole app via t().
TRANSLATIONS = {
    "app_name": {"en": "KaamSetu", "te": "కామ్‌సేతు", "hi": "कामसेतु"},
    "tagline": {"en": "Connecting Skills with Opportunities.",
                "te": "నైపుణ్యాలను అవకాశాలతో కలుపుతోంది.",
                "hi": "कौशल को अवसरों से जोड़ना।"},
    "subheading": {
        "en": "Find trusted skilled workers. Showcase your skills. Build your professional identity.",
        "te": "నమ్మకమైన నైపుణ్యం కలిగిన కార్మికులను కనుగొనండి. మీ నైపుణ్యాలను ప్రదర్శించండి.",
        "hi": "विश्वसनीय कुशल कामगार खोजें। अपने कौशल को प्रदर्शित करें। अपनी व्यावसायिक पहचान बनाएं।"},
    "register": {"en": "Register", "te": "నమోదు చేయండి", "hi": "पंजीकरण करें"},
    "login": {"en": "Login", "te": "లాగిన్", "hi": "लॉगिन"},
    "logout": {"en": "Logout", "te": "లాగ్అవుట్", "hi": "लॉगआउट"},
    "explore_workers": {"en": "Explore Workers", "te": "కార్మికులను చూడండి", "hi": "कामगार देखें"},
    "about_kaamsetu": {"en": "About KaamSetu", "te": "కామ్‌సేతు గురించి", "hi": "कामसेतु के बारे में"},
    "how_it_works": {"en": "How It Works", "te": "ఇది ఎలా పనిచేస్తుంది", "hi": "यह कैसे काम करता है"},
    "worker_categories": {"en": "Worker Categories", "te": "కార్మిక వర్గాలు", "hi": "कामगार श्रेणियाँ"},
    "trust_verification": {"en": "Trust & Verification", "te": "నమ్మకం & ధృవీకరణ", "hi": "विश्वास और सत्यापन"},
    "home": {"en": "Home", "te": "హోమ్", "hi": "होम"},
    "dashboard": {"en": "Dashboard", "te": "డాష్‌బోర్డ్", "hi": "डैशबोर्ड"},
    "customer": {"en": "Customer", "te": "వినియోగదారు", "hi": "ग्राहक"},
    "worker": {"en": "Worker", "te": "కార్మికుడు", "hi": "कामगार"},
    "admin": {"en": "Admin", "te": "అడ్మిన్", "hi": "एडमिन"},
    "name": {"en": "Name", "te": "పేరు", "hi": "नाम"},
    "email": {"en": "Email", "te": "ఇమెయిల్", "hi": "ईमेल"},
    "phone": {"en": "Phone", "te": "ఫోన్", "hi": "फ़ोन"},
    "password": {"en": "Password", "te": "పాస్‌వర్డ్", "hi": "पासवर्ड"},
    "location": {"en": "Location", "te": "ప్రాంతం", "hi": "स्थान"},
    "submit": {"en": "Submit", "te": "సమర్పించండి", "hi": "जमा करें"},
    "save": {"en": "Save", "te": "సేవ్ చేయండి", "hi": "सहेजें"},
    "cancel": {"en": "Cancel", "te": "రద్దు చేయండి", "hi": "रद्द करें"},
    "search": {"en": "Search", "te": "వెతకండి", "hi": "खोजें"},
    "filter": {"en": "Filter", "te": "ఫిల్టర్", "hi": "फ़िल्टर"},
    "view_profile": {"en": "View Profile", "te": "ప్రొఫైల్ చూడండి", "hi": "प्रोफ़ाइल देखें"},
    "request_work": {"en": "Request Work", "te": "పని అభ్యర్థించండి", "hi": "काम का अनुरोध करें"},
    "experience": {"en": "Experience", "te": "అనుభవం", "hi": "अनुभव"},
    "rating": {"en": "Rating", "te": "రేటింగ్", "hi": "रेटिंग"},
    "verified": {"en": "Verified", "te": "ధృవీకరించబడింది", "hi": "सत्यापित"},
    "pending_verification": {"en": "Pending Verification", "te": "ధృవీకరణ పెండింగ్‌లో ఉంది", "hi": "सत्यापन लंबित"},
    "not_verified": {"en": "Not Verified", "te": "ధృవీకరించబడలేదు", "hi": "असत्यापित"},
    "skills": {"en": "Skills", "te": "నైపుణ్యాలు", "hi": "कौशल"},
    "certificates": {"en": "Certificates", "te": "సర్టిఫికెట్లు", "hi": "प्रमाणपत्र"},
    "portfolio": {"en": "Portfolio", "te": "పోర్ట్‌ఫోలియో", "hi": "पोर्टफोलियो"},
    "work_requests": {"en": "Work Requests", "te": "పని అభ్యర్థనలు", "hi": "काम के अनुरोध"},
    "availability": {"en": "Availability", "te": "లభ్యత", "hi": "उपलब्धता"},
    "no_workers_found": {"en": "No workers found matching your criteria.",
                          "te": "మీ ప్రమాణాలకు సరిపోలే కార్మికులు కనుగొనబడలేదు.",
                          "hi": "आपके मानदंडों से मेल खाने वाला कोई कामगार नहीं मिला।"},
    "no_requests_yet": {"en": "No work requests yet.", "te": "ఇంకా పని అభ్యర్థనలు లేవు.", "hi": "अभी तक कोई काम अनुरोध नहीं।"},
    "no_portfolio": {"en": "No portfolio projects added yet.", "te": "ఇంకా పోర్ట్‌ఫోలియో ప్రాజెక్టులు జోడించలేదు.", "hi": "अभी तक कोई पोर्टफोलियो प्रोजेक्ट नहीं जोड़ा गया।"},
    "no_certificates": {"en": "No certificates uploaded yet.", "te": "ఇంకా సర్టిఫికెట్లు అప్‌లోడ్ చేయలేదు.", "hi": "अभी तक कोई प्रमाणपत्र अपलोड नहीं किया गया।"},
    "no_reviews": {"en": "No reviews available yet.", "te": "ఇంకా సమీక్షలు అందుబాటులో లేవు.", "hi": "अभी तक कोई समीक्षा उपलब्ध नहीं।"},
    "trusted_worker_badge": {"en": "KaamSetu Trusted Worker", "te": "కామ్‌సేతు నమ్మకమైన కార్మికుడు", "hi": "कामसेतु विश्वसनीय कामगार"},
    "recommended_for_you": {"en": "Recommended Workers for You", "te": "మీ కోసం సిఫార్సు చేయబడిన కార్మికులు", "hi": "आपके लिए अनुशंसित कामगार"},
    "match": {"en": "Match", "te": "మ్యాచ్", "hi": "मैच"},

    # --- Navigation labels ---
    "find_a_worker": {"en": "Find a Worker", "te": "కార్మికుడిని కనుగొనండి", "hi": "कामगार खोजें"},
    "smart_matching": {"en": "Smart Matching", "te": "స్మార్ట్ మ్యాచింగ్", "hi": "स्मार्ट मैचिंग"},
    "my_profile": {"en": "My Profile", "te": "నా ప్రొఫైల్", "hi": "मेरी प्रोफ़ाइल"},
    "my_requests": {"en": "My Requests", "te": "నా అభ్యర్థనలు", "hi": "मेरे अनुरोध"},
    "bookings": {"en": "Bookings", "te": "బుకింగ్‌లు", "hi": "बुकिंग"},
    "jobs": {"en": "Jobs", "te": "ఉద్యోగాలు", "hi": "काम"},
    "notifications": {"en": "Notifications", "te": "నోటిఫికేషన్లు", "hi": "सूचनाएं"},
    "settings": {"en": "Settings", "te": "సెట్టింగ్‌లు", "hi": "सेटिंग्स"},
    "experience_label": {"en": "Experience", "te": "అనుభవం", "hi": "अनुभव"},
    "verification": {"en": "Verification", "te": "ధృవీకరణ", "hi": "सत्यापन"},
    "preview_public_profile": {"en": "Preview Public Profile", "te": "పబ్లిక్ ప్రొఫైల్‌ను ప్రివ్యూ చేయండి", "hi": "सार्वजनिक प्रोफ़ाइल का पूर्वावलोकन करें"},
    "overview": {"en": "Overview", "te": "అవలోకనం", "hi": "अवलोकन"},
    "customers": {"en": "Customers", "te": "వినియోగదారులు", "hi": "ग्राहक"},
    "workers": {"en": "Workers", "te": "కార్మికులు", "hi": "कामगार"},
    "reviews": {"en": "Reviews", "te": "సమీక్షలు", "hi": "समीक्षाएं"},
    "categories": {"en": "Categories", "te": "వర్గాలు", "hi": "श्रेणियां"},
    "back": {"en": "Back", "te": "వెనుకకు", "hi": "वापस"},

    # --- Smart Matching feature ---
    "best_matches_for_you": {"en": "Best Matches for You", "te": "మీ కోసం ఉత్తమ మ్యాచ్‌లు", "hi": "आपके लिए सर्वश्रेष्ठ मैच"},
    "match_score": {"en": "Match Score", "te": "మ్యాచ్ స్కోర్", "hi": "मैच स्कोर"},
    "why_this_worker_matches": {"en": "Why this worker matches", "te": "ఈ కార్మికుడు ఎందుకు సరిపోతాడు", "hi": "यह कामगार क्यों उपयुक्त है"},
    "book_worker": {"en": "Book Worker", "te": "కార్మికుడిని బుక్ చేయండి", "hi": "कामगार बुक करें"},
    "no_exact_match_found": {"en": "No exact match found.", "te": "ఖచ్చితమైన మ్యాచ్ కనుగొనబడలేదు.", "hi": "कोई सटीक मैच नहीं मिला।"},
    "closest_available_workers": {"en": "Here are the closest available workers instead:",
                                   "te": "బదులుగా అందుబాటులో ఉన్న అత్యంత దగ్గరి కార్మికులు ఇక్కడ ఉన్నారు:",
                                   "hi": "इसके बजाय यहां निकटतम उपलब्ध कामगार हैं:"},
    "completed_projects": {"en": "Completed Projects", "te": "పూర్తయిన ప్రాజెక్టులు", "hi": "पूर्ण परियोजनाएं"},
    "work_category": {"en": "Work Category", "te": "పని వర్గం", "hi": "कार्य श्रेणी"},
    "required_skill": {"en": "Required Skill", "te": "అవసరమైన నైపుణ్యం", "hi": "आवश्यक कौशल"},
    "min_experience_required": {"en": "Minimum Experience Required (years)", "te": "కనీస అనుభవం అవసరం (సంవత్సరాలు)", "hi": "न्यूनतम आवश्यक अनुभव (वर्ष)"},
    "budget_range": {"en": "Budget Range (₹)", "te": "బడ్జెట్ పరిధి (₹)", "hi": "बजट सीमा (₹)"},
    "preferred_availability": {"en": "Preferred Availability", "te": "ప్రాధాన్య లభ్యత", "hi": "पसंदीदा उपलब्धता"},
    "urgency": {"en": "Urgency", "te": "అత్యవసరత", "hi": "तात्कालिकता"},
    "work_description_optional": {"en": "Description of the work (optional)", "te": "పని వివరణ (ఐచ్ఛికం)", "hi": "काम का विवरण (वैकल्पिक)"},
    "find_best_matches": {"en": "Find Best Matches", "te": "ఉత్తమ మ్యాచ్‌లను కనుగొనండి", "hi": "सर्वश्रेष्ठ मैच खोजें"},
    "expand_location": {"en": "Expand your location radius", "te": "మీ ప్రాంత పరిధిని విస్తరించండి", "hi": "अपनी स्थान सीमा बढ़ाएं"},
    "increase_budget": {"en": "Increase your budget", "te": "మీ బడ్జెట్‌ను పెంచండి", "hi": "अपना बजट बढ़ाएं"},
    "choose_other_availability": {"en": "Choose another availability time", "te": "మరొక లభ్యత సమయాన్ని ఎంచుకోండి", "hi": "एक और उपलब्धता समय चुनें"},
    "select_related_skills": {"en": "Select related skills/categories", "te": "సంబంధిత నైపుణ్యాలు/వర్గాలను ఎంచుకోండి", "hi": "संबंधित कौशल/श्रेणियां चुनें"},
    "suggestions": {"en": "Suggestions", "te": "సూచనలు", "hi": "सुझाव"},
    "no_notifications": {"en": "No notifications yet.", "te": "ఇంకా నోటిఫికేషన్లు లేవు.", "hi": "अभी तक कोई सूचना नहीं।"},
    "account_settings": {"en": "Account Settings", "te": "ఖాతా సెట్టింగ్‌లు", "hi": "खाता सेटिंग्स"},

    # --- Auth pages / misc chrome ---
    "already_have_account": {"en": "Already have an account?", "te": "ఇప్పటికే ఖాతా ఉందా?", "hi": "पहले से खाता है?"},
    "dont_have_account": {"en": "Don't have an account?", "te": "ఖాతా లేదా?", "hi": "खाता नहीं है?"},
    "login_instead": {"en": "Login instead", "te": "బదులుగా లాగిన్ చేయండి", "hi": "इसके बजाय लॉगिन करें"},
    "register_instead": {"en": "Register instead", "te": "బదులుగా నమోదు చేయండి", "hi": "इसके बजाय पंजीकरण करें"},
    "email_or_phone": {"en": "Email or Phone", "te": "ఇమెయిల్ లేదా ఫోన్", "hi": "ईमेल या फ़ोन"},
    "confirm_password": {"en": "Confirm Password", "te": "పాస్‌వర్డ్‌ను నిర్ధారించండి", "hi": "पासवर्ड की पुष्टि करें"},
    "i_am_a": {"en": "I am a:", "te": "నేను ఒక:", "hi": "मैं हूँ:"},
    "register_as": {"en": "Register as:", "te": "వీరిగా నమోదు చేయండి:", "hi": "इस रूप में पंजीकरण करें:"},
    "welcome_back": {"en": "Welcome back", "te": "తిరిగి స్వాగతం", "hi": "वापसी पर स्वागत है"},
    "return_to_home": {"en": "Return to Home", "te": "హోమ్‌కు తిరిగి వెళ్లండి", "hi": "होम पर वापस जाएं"},

    # --- Landing page body copy ---
    "about_kaamsetu_body": {
        "en": "KaamSetu is a skilled-worker discovery and connection platform built on one simple idea: "
              "every skilled worker deserves a trusted, professional digital identity. Instead of a "
              "one-line listing, every worker gets a full professional portfolio — skills, verified "
              "certificates, real project photos, work history, and genuine customer reviews — so "
              "customers can hire with confidence.",
        "te": "కామ్‌సేతు అనేది నైపుణ్యం కలిగిన కార్మికులను కనుగొని కలుపుకునే వేదిక, ఒక సాధారణ ఆలోచనపై నిర్మించబడింది: "
              "ప్రతి నైపుణ్యం కలిగిన కార్మికుడు నమ్మకమైన, వృత్తిపరమైన డిజిటల్ గుర్తింపుకు అర్హుడు. ప్రతి కార్మికుడికి "
              "పూర్తి వృత్తిపరమైన పోర్ట్‌ఫోలియో లభిస్తుంది — నైపుణ్యాలు, ధృవీకరించిన సర్టిఫికెట్లు, నిజమైన ప్రాజెక్ట్ ఫోటోలు, "
              "పని చరిత్ర, మరియు నిజమైన వినియోగదారు సమీక్షలు — తద్వారా వినియోగదారులు నమ్మకంతో నియమించుకోవచ్చు.",
        "hi": "कामसेतु एक कुशल-कामगार खोज और जुड़ाव मंच है जो एक सरल विचार पर बना है: हर कुशल कामगार एक "
              "विश्वसनीय, व्यावसायिक डिजिटल पहचान का हकदार है। एक-पंक्ति की सूची के बजाय, हर कामगार को एक पूर्ण "
              "व्यावसायिक पोर्टफोलियो मिलता है — कौशल, सत्यापित प्रमाणपत्र, वास्तविक परियोजना तस्वीरें, कार्य इतिहास, "
              "और वास्तविक ग्राहक समीक्षाएं — ताकि ग्राहक विश्वास के साथ नियुक्त कर सकें।",
    },
    "step_discover_title": {"en": "Discover", "te": "కనుగొనండి", "hi": "खोजें"},
    "step_discover_desc": {"en": "Search verified skilled workers by category, skill, location, or rating.",
                            "te": "వర్గం, నైపుణ్యం, ప్రాంతం లేదా రేటింగ్ ద్వారా ధృవీకరించిన కార్మికులను వెతకండి.",
                            "hi": "श्रेणी, कौशल, स्थान या रेटिंग के आधार पर सत्यापित कामगार खोजें।"},
    "step_portfolio_title": {"en": "View Portfolio", "te": "పోర్ట్‌ఫోలియో చూడండి", "hi": "पोर्टफोलियो देखें"},
    "step_portfolio_desc": {"en": "Browse real certificates, past projects, and customer reviews.",
                             "te": "నిజమైన సర్టిఫికెట్లు, గత ప్రాజెక్టులు, వినియోగదారు సమీక్షలను చూడండి.",
                             "hi": "वास्तविक प्रमाणपत्र, पिछली परियोजनाएं और ग्राहक समीक्षाएं देखें।"},
    "step_request_title": {"en": "Request Work", "te": "పని అభ్యర్థించండి", "hi": "काम का अनुरोध करें"},
    "step_request_desc": {"en": "Send a work request with your requirements and preferred schedule.",
                           "te": "మీ అవసరాలు మరియు ప్రాధాన్య షెడ్యూల్‌తో పని అభ్యర్థన పంపండి.",
                           "hi": "अपनी आवश्यकताओं और पसंदीदा समय के साथ कार्य अनुरोध भेजें।"},
    "step_review_title": {"en": "Rate & Review", "te": "రేట్ చేసి సమీక్షించండి", "hi": "रेट करें और समीक्षा करें"},
    "step_review_desc": {"en": "Once work is completed, rate the worker and build the trust ecosystem.",
                          "te": "పని పూర్తయిన తర్వాత, కార్మికుడిని రేట్ చేసి నమ్మక వ్యవస్థను నిర్మించండి.",
                          "hi": "काम पूरा होने के बाद, कामगार को रेट करें और विश्वास तंत्र बनाएं।"},
    "trust1_title": {"en": "Admin-Reviewed Verification", "te": "అడ్మిన్-సమీక్షించిన ధృవీకరణ", "hi": "एडमिन-समीक्षित सत्यापन"},
    "trust1_desc": {"en": "Workers submit documents; only our admin team can approve or reject verification.",
                     "te": "కార్మికులు పత్రాలను సమర్పిస్తారు; మా అడ్మిన్ బృందం మాత్రమే ధృవీకరణను ఆమోదించగలదు లేదా తిరస్కరించగలదు.",
                     "hi": "कामगार दस्तावेज़ जमा करते हैं; केवल हमारी एडमिन टीम ही सत्यापन को मंजूर या अस्वीकार कर सकती है।"},
    "trust2_title": {"en": "KaamSetu Trusted Worker Badge", "te": "కామ్‌సేతు నమ్మకమైన కార్మికుడు బ్యాడ్జ్", "hi": "कामसेतु विश्वसनीय कामगार बैज"},
    "trust2_desc": {"en": "Awarded only when a worker meets a minimum completed-project and rating threshold.",
                     "te": "కార్మికుడు కనీస పూర్తయిన ప్రాజెక్టులు మరియు రేటింగ్ పరిమితిని చేరుకున్నప్పుడు మాత్రమే ఇవ్వబడుతుంది.",
                     "hi": "यह तभी दिया जाता है जब कामगार न्यूनतम पूर्ण-परियोजना और रेटिंग सीमा को पूरा करता है।"},
    "trust3_title": {"en": "Genuine Reviews", "te": "నిజమైన సమీక్షలు", "hi": "वास्तविक समीक्षाएं"},
    "trust3_desc": {"en": "Only customers with a completed work request can leave one review — no fake ratings.",
                     "te": "పూర్తయిన పని అభ్యర్థన ఉన్న వినియోగదారులు మాత్రమే ఒక సమీక్షను వదలగలరు — నకిలీ రేటింగ్‌లు లేవు.",
                     "hi": "केवल पूर्ण कार्य अनुरोध वाले ग्राहक ही एक समीक्षा छोड़ सकते हैं — कोई नकली रेटिंग नहीं।"},
    "browse_workers_hint": {"en": "Browse verified skilled workers. Log in or register to send a work request.",
                             "te": "ధృవీకరించిన కార్మికులను చూడండి. పని అభ్యర్థన పంపడానికి లాగిన్ లేదా నమోదు చేయండి.",
                             "hi": "सत्यापित कामगारों को देखें। कार्य अनुरोध भेजने के लिए लॉगिन या पंजीकरण करें।"},
    "login_or_register_hint": {"en": "Log in or register as a Customer to view the full profile or send a request.",
                                "te": "పూర్తి ప్రొఫైల్ చూడటానికి లేదా అభ్యర్థన పంపడానికి వినియోగదారుగా లాగిన్ లేదా నమోదు చేయండి.",
                                "hi": "पूर्ण प्रोफ़ाइल देखने या अनुरोध भेजने के लिए ग्राहक के रूप में लॉगिन या पंजीकरण करें।"},
    "workers_found": {"en": "worker(s) found", "te": "కార్మికులు కనుగొనబడ్డారు", "hi": "कामगार मिले"},
    "workers_available": {"en": "worker(s) available", "te": "కార్మికులు అందుబాటులో ఉన్నారు", "hi": "कामगार उपलब्ध"},

    # --- Settings / change password ---
    "current_password": {"en": "Current Password", "te": "ప్రస్తుత పాస్‌వర్డ్", "hi": "वर्तमान पासवर्ड"},
    "new_password": {"en": "New Password", "te": "కొత్త పాస్‌వర్డ్", "hi": "नया पासवर्ड"},
    "confirm_new_password": {"en": "Confirm New Password", "te": "కొత్త పాస్‌వర్డ్‌ను నిర్ధారించండి", "hi": "नया पासवर्ड की पुष्टि करें"},
    "change_password": {"en": "Change Password", "te": "పాస్‌వర్డ్ మార్చండి", "hi": "पासवर्ड बदलें"},
    "password_changed": {"en": "Password changed successfully!", "te": "పాస్‌వర్డ్ విజయవంతంగా మార్చబడింది!", "hi": "पासवर्ड सफलतापूर्वक बदल दिया गया!"},
    "account_info": {"en": "Account Information", "te": "ఖాతా సమాచారం", "hi": "खाता जानकारी"},

    # --- Common actions used across dashboards ---
    "add": {"en": "Add", "te": "జోడించండి", "hi": "जोड़ें"},
    "delete": {"en": "Delete", "te": "తొలగించండి", "hi": "हटाएं"},
    "upload": {"en": "Upload", "te": "అప్‌లోడ్ చేయండి", "hi": "अपलोड करें"},
    "all_categories": {"en": "All Categories", "te": "అన్ని వర్గాలు", "hi": "सभी श्रेणियां"},
    "any_category": {"en": "Any Category", "te": "ఏదైనా వర్గం", "hi": "कोई भी श्रेणी"},
    "any": {"en": "Any", "te": "ఏదైనా", "hi": "कोई भी"},
    "description": {"en": "Description", "te": "వివరణ", "hi": "विवरण"},
    "status_pending": {"en": "Pending", "te": "పెండింగ్‌లో ఉంది", "hi": "लंबित"},
    "status_accepted": {"en": "Accepted", "te": "ఆమోదించబడింది", "hi": "स्वीकृत"},
    "status_rejected": {"en": "Rejected", "te": "తిరస్కరించబడింది", "hi": "अस्वीकृत"},
    "status_in_progress": {"en": "In Progress", "te": "ప్రగతిలో ఉంది", "hi": "प्रगति पर"},
    "status_completed": {"en": "Completed", "te": "పూర్తయింది", "hi": "पूर्ण"},
    "status_cancelled": {"en": "Cancelled", "te": "రద్దు చేయబడింది", "hi": "रद्द"},
    "welcome_comma": {"en": "Welcome", "te": "స్వాగతం", "hi": "स्वागत है"},
    "no_skills_yet": {"en": "No skills added yet.", "te": "ఇంకా నైపుణ్యాలు జోడించలేదు.", "hi": "अभी तक कोई कौशल नहीं जोड़ा गया।"},
    "no_experience_yet": {"en": "No work experience added yet.", "te": "ఇంకా పని అనుభవం జోడించలేదు.", "hi": "अभी तक कोई कार्य अनुभव नहीं जोड़ा गया।"},
    "about": {"en": "About", "te": "గురించి", "hi": "बारे में"},

    # --- Security Deposit ---
    "security_deposit": {"en": "Security Deposit", "te": "భద్రతా డిపాజిట్", "hi": "सुरक्षा जमा राशि"},
    "deposit_required": {"en": "₹200 Deposit Required", "te": "₹200 డిపాజిట్ అవసరం", "hi": "₹200 जमा राशि आवश्यक"},
    "deposit_paid": {"en": "Deposit Paid", "te": "డిపాజిట్ చెల్లించబడింది", "hi": "जमा राशि भुगतान की गई"},
    "project_completed": {"en": "Project Completed", "te": "ప్రాజెక్ట్ పూర్తయింది", "hi": "परियोजना पूर्ण"},
    "refund_processed": {"en": "₹200 Refund Processed", "te": "₹200 వాపసు ప్రాసెస్ చేయబడింది", "hi": "₹200 धनवापसी संसाधित"},
    "pay_deposit_button": {"en": "Pay ₹200 Deposit (Simulated)", "te": "₹200 డిపాజిట్ చెల్లించండి (అనుకరణ)", "hi": "₹200 जमा राशि भुगतान करें (सिम्युलेटेड)"},
    "deposit_amount": {"en": "Deposit Amount", "te": "డిపాజిట్ మొత్తం", "hi": "जमा राशि"},
    "deposit_status": {"en": "Deposit Status", "te": "డిపాజిట్ స్థితి", "hi": "जमा स्थिति"},
    "refund_status": {"en": "Refund Status", "te": "వాపసు స్థితి", "hi": "धनवापसी स्थिति"},
    "no_deposit_required_yet": {"en": "No security deposit on file yet — one will be requested with your first booking.",
                                  "te": "ఇంకా భద్రతా డిపాజిట్ లేదు — మీ మొదటి బుకింగ్‌తో అభ్యర్థించబడుతుంది.",
                                  "hi": "अभी तक कोई सुरक्षा जमा राशि दर्ज नहीं है — आपकी पहली बुकिंग के साथ इसका अनुरोध किया जाएगा।"},
    "no_deposit_required_yet_worker": {"en": "No security deposit on file yet — one will be requested when you accept your first project.",
                                         "te": "ఇంకా భద్రతా డిపాజిట్ లేదు — మీరు మీ మొదటి ప్రాజెక్ట్‌ను ఆమోదించినప్పుడు అభ్యర్థించబడుతుంది.",
                                         "hi": "अभी तक कोई सुरक्षा जमा राशि दर्ज नहीं है — जब आप अपनी पहली परियोजना स्वीकार करेंगे तब इसका अनुरोध किया जाएगा।"},
    "deposit_note": {"en": "This is a refundable deposit, not a service fee — it is fully refunded once your first "
                            "project is completed (or unchanged if it's cancelled).",
                      "te": "ఇది వాపసు చేయదగిన డిపాజిట్, సేవా రుసుము కాదు — మీ మొదటి ప్రాజెక్ట్ పూర్తయిన తర్వాత పూర్తిగా వాపసు చేయబడుతుంది.",
                      "hi": "यह एक वापसी योग्य जमा राशि है, सेवा शुल्क नहीं — आपकी पहली परियोजना पूर्ण होने पर यह पूरी तरह वापस कर दी जाती है।"},
    "deposits": {"en": "Deposits", "te": "డిపాజిట్లు", "hi": "जमा राशियाँ"},
    "not_applicable": {"en": "Not Applicable", "te": "వర్తించదు", "hi": "लागू नहीं"},
    "linked_booking_status": {"en": "Linked Booking/Project Status", "te": "అనుసంధాన బుకింగ్/ప్రాజెక్ట్ స్థితి", "hi": "जुड़ी बुकिंग/परियोजना स्थिति"},
    "no_deposits_yet": {"en": "No security deposits recorded yet.", "te": "ఇంకా భద్రతా డిపాజిట్‌లు నమోదు కాలేదు.", "hi": "अभी तक कोई सुरक्षा जमा राशि दर्ज नहीं है।"},
}


def t(key: str, lang_code: str = "en") -> str:
    """Translate a key into the given language code, falling back to English."""
    entry = TRANSLATIONS.get(key)
    if not entry:
        return key.replace("_", " ").title()
    return entry.get(lang_code, entry.get("en", key))


# ---------------------------------------------------------------------------
# REFUNDABLE SECURITY DEPOSIT
# ---------------------------------------------------------------------------
SECURITY_DEPOSIT_AMOUNT = 200  # ₹200, refundable - required once per user (customer/worker)
REQUEST_STATUSES = ["Pending", "Accepted", "Rejected", "In Progress", "Completed", "Cancelled"]

# ---------------------------------------------------------------------------
# VERIFICATION STATUSES
# ---------------------------------------------------------------------------
VERIFICATION_STATUSES = ["Pending", "Verified", "Rejected"]

AVAILABILITY_STATES = ["Available", "Busy", "Currently Unavailable"]
