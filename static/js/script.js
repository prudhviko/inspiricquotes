function shareOnFacebook(shareUrl) {
    const facebookUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(shareUrl)}`;
    window.open(facebookUrl, '_blank');
}

function shareOnTwitter(shareUrl) {
    const twitterUrl = `https://twitter.com/intent/tweet?url=${encodeURIComponent(shareUrl)}`;
    window.open(twitterUrl, '_blank');
}

function shareOnLinkedIn(shareUrl) {
    const linkedinUrl = `https://www.linkedin.com/shareArticle?mini=true&url=${encodeURIComponent(shareUrl)}`;
    window.open(linkedinUrl, '_blank');
}

function shareOnInstagram(shareUrl) {
    const instagramUrl = `https://www.instagram.com/create/?url=${encodeURIComponent(shareUrl)}`;
    window.open(instagramUrl, '_blank');
}

function shareOnTelegram(shareUrl,shareText) {
    const telegramUrl = `https://t.me/share/url?url=${encodeURIComponent(shareUrl)}&text=${encodeURIComponent(shareText)}`;
    window.open(telegramUrl, '_blank');
}

function shareOnWhatsApp(shareUrl,shareText) {
    const sT = `${shareUrl}`
    console.log(sT)
    const whatsappUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(sT)}`;
    window.open(whatsappUrl, '_blank');
}