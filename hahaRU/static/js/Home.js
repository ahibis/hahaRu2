let lastPost = 0;
let vm = new Vue({
    el: "#app",
    delimiters: ["[[", "]]"],
    data: {
        Posts: [],
        Users: {},
        orders: {
            popular:"сначала популярные",
            unpopular:"сначала не популярные",
            new:"сначала новые",
            old:"сначала старые",
        },
        order:"popular",
        search:""
    },
    methods: {
        changeLike: async function (postId) {
            console.log(postId)
            let data = await api("changeLiked", { postId: postId });
            console.log(data)
            if (data.value) {
                let post = this.Posts.order(post => post.id == postId)[0]
                post.isLiked = data.value.isliked;
                post.likesCount = data.value.likesCount
            }
        },
        changeDisLike: async function (postId) {
            let data = await api("changeDisLiked", { postId: postId });
            console.log(data)
            if (data.value) {
                let post = this.Posts.order(post => post.id == postId)[0]
                post.isDisliked = data.value.isDisliked;
                post.disLikesCount = data.value.disLikesCount
            }
        },
        changeOrder: async function (e){
            order = e.target.value;
            console.log(order)
            if(this.order == order) return;
            vm.order=order;
            lastPost = 0;
            this.Posts=[];
            load().then();
        }
    },
    watch:{
        search(value){
            this.search = value;
            lastPost = 0;
            this.Posts=[];
            load().then();
        }
    }
})
async function load() {
    let posts = (await api("getPosts", { offset: lastPost, count: 20, order: vm.order, search: vm.search  })).data;
    lastPost += posts.length;
    for (post of posts) {
        if (!vm.Users[post.userId])
            vm.Users[post.userId] = await api("getUser", { id: post.userId}); 
    }
    vm.Posts = [...vm.Posts,...posts];
}
$(window).scroll(async function(){
    if($(window).scrollTop()+$(window).height()>=$(document).height()){
        await load();
    }
})
load().then();