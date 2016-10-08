'use strict';

(function () {
    // settings for ajax - getting cookie
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == name + '=') {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method)
        );
    }

    function updateIdeaData(data) {
        $current_funders.html(data.get_current_funders);
        $current_quantity.html(data.get_current_quantity);
        $current_progress.attr('style', 'width:' + data.get_current_progress + "%");
    }

    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function beforeSend(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    var CommentForm = React.createClass({
        displayName: 'CommentForm',

        getInitialState: function getInitialState() {
            return { content: '' };
        },
        handleContentChange: function handleContentChange(e) {
            if (this.isMounted()) {
                this.setState({ content: e.target.value });
            }
        },
        handleSubmit: function handleSubmit(e) {
            e.preventDefault();
            var content = this.state.content.trim();
            this.props.onCommentSubmit({ content: content });
            if (this.isMounted()) {
                this.setState({ content: '' });
            }
        },
        render: function render() {
            return React.createElement(
                'div',
                { className: 'form-group' },
                React.createElement(
                    'form',
                    { className: 'commentForm', onSubmit: this.handleSubmit },
                    React.createElement('textarea', {
                        className: 'form-control',
                        placeholder: 'Comment',
                        value: this.state.content,
                        onChange: this.handleContentChange,
                        required: true
                    }),
                    React.createElement('input', {
                        className: 'btn btn-primary',
                        type: 'submit',
                        value: 'Post'
                    })
                )
            );
        }
    });

    var Text = React.createClass({
        displayName: 'Text',

        render: function render() {
            return React.createElement(
                'div',
                { className: 'media-body' },
                React.createElement(
                    'h5',
                    { className: 'media-heading' },
                    this.props.content
                ),
                React.createElement(
                    'p',
                    null,
                    this.props.username
                )
            );
        }
    });

    var Photo = React.createClass({
        displayName: 'Photo',

        render: function render() {
            var divStyle = {
                height: 64,
                width: 64,
                borderRadius: 50,
                backgroundSize: 'cover',
                backgroundImage: 'url(' + this.props.src + ')'
            };
            return React.createElement(
                'div',
                { className: 'media-left media-middle' },
                React.createElement('div', { className: 'media-object', style: divStyle })
            );
        }
    });

    var Comment = React.createClass({
        displayName: 'Comment',

        render: function render() {
            return React.createElement(
                'div',
                { className: 'media' },
                React.createElement(Photo, { src: this.props.src }),
                React.createElement(Text, {
                    username: this.props.username,
                    content: this.props.content,
                    created_at: this.props.created_at
                })
            );
        }
    });

    var CommentList = React.createClass({
        displayName: 'CommentList',

        render: function render() {
            var commentNodes = {};
            commentNodes = this.props.data.map(function (comment) {
                return React.createElement(Comment, {
                    key: comment.id,
                    username: comment.username,
                    src: comment.user_profileimage_url,
                    created_at: comment.created_at,
                    content: comment.content
                });
            });
            return React.createElement(
                'div',
                { className: 'commentList' },
                commentNodes
            );
        }
    });

    var CommentBox = React.createClass({
        displayName: 'CommentBox',

        loadCommentsFromServer: function loadCommentsFromServer() {
            $.ajax({
                url: this.props.url + "/",
                dataType: 'json',
                cache: false,
                success: function (data) {
                    if (this.isMounted()) {
                        this.setState({ data: data });
                    }
                }.bind(this),
                error: function (xhr, status, err) {
                    console.error(this.props.url, status, err.toString());
                }.bind(this)
            });
        },
        handleCommentSubmit: function handleCommentSubmit(comment) {
            $.ajax({
                url: this.props.url + "/",
                dataType: 'json',
                type: 'POST',
                data: comment,
                success: function (data) {
                    if (this.isMounted()) {
                        this.setState({ data: data });
                    }
                }.bind(this),
                error: function (xhr, status, err) {
                    console.error(this.props.url, status, err.toString());
                }.bind(this)
            });
        },
        getInitialState: function getInitialState() {
            return { data: [] };
        },
        componentDidMount: function componentDidMount() {
            this.loadCommentsFromServer();
            setInterval(this.loadCommentsFromServer, this.props.pollInterval);
        },
        render: function render() {
            return React.createElement(
                'div',
                null,
                React.createElement(CommentList, { data: this.state.data }),
                React.createElement(CommentForm, { onCommentSubmit: this.handleCommentSubmit })
            );
        }
    });

    var idea_url = "/ideas/explore/" + $('#comment-box').data('idea-id') + "/comment";

    $(document).ready(function () {

        ReactDOM.render(React.createElement(CommentBox, { url: idea_url, pollInterval: 1500 }), document.getElementById('comment-box'));
    });
})();
